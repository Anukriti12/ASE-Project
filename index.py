# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 23:20:38 2020

@author: anukriti
"""

#importing libraries
import pickle
import inputScript

#load the pickle file
classifier = pickle.load(open('final_models/svm_final.pkl', 'rb'))


#input url
print("enter url")
url = input()

#checking and predicting
checkprediction = inputScript.main(url)
prediction = classifier.predict(checkprediction)
print(prediction)
