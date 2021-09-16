import flask
import pickle
import os
import pandas as pd
import numpy as np

port = int(os.getenv("PORT", 8080))
app = flask.Flask(__name__, template_folder='./')

fileDir = os.path.dirname(os.path.realpath('__file__'))

fileName = "app/deploy/decissiontreemodel.pkl"

filePath = os.path.join(fileDir, fileName)

with open(filePath, 'rb') as f:
        model = pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':

        Education = flask.request.form['Education']
        Sex = flask.request.form['Sex']
        Age = flask.request.form['Age']
        if int(Age) <= 70:
            Age = 0
        elif int(Age) <= 72:
            Age = 1
        elif int(Age) <= 74:
            Age = 2
        elif int(Age) <= 76:
            Age = 3
        elif int(Age) <= 78:
            Age = 4
        else:
            Age = 5
        Sport = flask.request.form['Sport']
        Children = flask.request.form['Children']
        Pet = flask.request.form['Pet']
        if int(Pet) + int(Children) == 0:
            IsAlone = 1
        else:
            IsAlone = 0
        input_variables = pd.DataFrame([[Education,Sex,Age,Sport,IsAlone,Children,Pet]],
                                       columns=['Education','Sex','Age','Sport','IsAlone','Children','Pet'],
                                       dtype=np.int64)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('main.html',
                                     original_input={'Education':Education,'Sex':Sex,'Age':Age,'Sport':Sport,'Children':Children,'Pet':Pet},
                                     result=prediction,
                                     )
