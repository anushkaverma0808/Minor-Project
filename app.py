# -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template
#from flask import Flask

# Load ML model
model = pickle.load(open('model.pkl', 'rb'))

# Create application
app = Flask(__name__)


# Bind home function to URL
@app.route('/form')
def home():
    return render_template('minorproject.html')

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/loc')
def location_doc():
    return render_template('loc.html')



# Bind predict function to URL
@app.route('/predict', methods=['POST'])
def predict():
    # Put all form entries values in a list
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)

    output = prediction

    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('minorproject.html',
                               result='The patient is not likely to have heart disease!')
    else:
        return render_template('minorproject.html',
                               result='The patient is likely to have heart disease!')


if __name__ == '__main__':
    # Run the application
    app.run()


