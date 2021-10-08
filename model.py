import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('Data.csv',encoding="ISO-8859-1")

train = df[df['Date'] < '20150101']
test =df[df['Date'] > '20141231']

# removing punctuations
data = train.iloc[:,2:27]
data.replace ("[^a-zA-Z]"," ",regex=True,inplace=True)

#renaming column for ease of access
list1=[i for i in range(25)]
new_Index = [str(i) for i in list1]
data.columns = new_Index

#converting into lowercase
for index in new_Index:
    data[index] = data[index].str.lower()
data.head(5)

#joininf all sentance in one with spacing
headlines=[]
for rows in range(0,len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[rows,0:25]))

# implement BAG OF WORDS
tfidfvector = TfidfVectorizer(ngram_range=(2,2))
traindataset= tfidfvector.fit_transform(headlines)

#creating encoding pickel file 
pickle.dump(tfidfvector,open('transform.pkl','wb'))

#traning model
randomclassifier=RandomForestClassifier(n_estimators=200,criterion='entropy')
randomclassifier.fit(traindataset,train['Label'])

#creating model pickel file
pickle.dump(randomclassifier, open('model.pkl', 'wb'))

