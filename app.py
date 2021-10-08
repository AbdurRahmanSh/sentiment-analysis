from flask import Flask,request,render_template
import pickle
import pandas as pd

app = Flask(__name__)

cv = pickle.load(open('transform.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        textword = request.form['message']
        data = [textword]
        vect = cv.transform(data)
        my_predict = model.predict(vect)
    return render_template('index.html',prediction = my_predict)

   
if __name__ == '__main__':
    app.run(debug=True)

