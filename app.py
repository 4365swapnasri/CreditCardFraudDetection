


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.linear_model import LogisticRegression

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/check')
def check():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = int(request.form['before_transaction'])
        user_input1 = int(request.form['after_transaction'])
        user_input2 = int(request.form['time'])
        user_input3 = int(request.form['card_number'])
        user_input4 = int(request.form['verification_number'])

        l = [user_input, user_input1, user_input2, user_input3, user_input4]

        nn = list(np.random.rand(24))
        ss = l + nn
        fun = np.array(ss)
        fun = fun.reshape(1, 29)

        pred = model.predict(fun)
        if pred == [1]:
            sss = "FRAUD"
        else:
            sss = "your tranisition is legitimate "

        return render_template('output.html', prediction=sss)

if __name__ == '__main__':
    app.run(debug=True)