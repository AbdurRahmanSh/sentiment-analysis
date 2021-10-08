
# Overview
We have used various machine Learning Algorithms from Sklearn such as Randomforest,catboost,xgboost,NavieBaysien.
This App try to predict are stock going to raise or fall based on news headline this whole project is based on stock nwes sentimation analysis.

# Acknowledgements
 ## Tasks perform on data
    1. Data was collected from Kaggle [https://www.kaggle.com/rohit0906/stock-sentiment-analysis-using-news-headlines]
    2. Dataset contains label[0 and 1] Ans Top name columns range of 1 to 25.Here 1 means stocks goind to raise and 0 means stock going to fall.
    3. WE performed regex opreation to remove all special characters and replace with blank space.
    4. We have converted data into lowercase and perform BAG of WORDS by merging all columns to get one sentences.
    5. Data has been split into train and test set.
    6. train dataset is used for training model.
    7. Pickle file has been generated with best model.
    8. Deployed in heroku Platform.
## Tech Stack

**Packages:** Sklearn, Flask, Python 3.8

**API:** Heruku, Github

**Software:** vscode,nicepage

  
## Installation

Installation of package.Preferd to make new Environment

```bash
  pip install -r requirements.txt
```
    
## Environment Variables

To run this project, we have to create new Enviroment

https://docs.python.org/3/library/venv.html

  ## Creating in Anaconda
  https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

  
## Credits

- Nobel Xavier
- Krish Naik [https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig]
- Kaggle
- Google
-NicePage [https://nicepage.com/]

  
## Project Screenshots

![App Screenshot] (stock sementic.gif)

  
## 🔗 Links
[![Heroku](https://img.shields.io/badge/Heroku-sentiment--analysis-yellowgreen?style=for-the-badge&logo=ko-fi&logoColor=white)](https://stocksentimentanalyis.herokuapp.com/)

