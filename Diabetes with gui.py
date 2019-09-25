from pandas import ExcelWriter
from sklearn import linear_model
import pandas as pd
from pandas import DataFrame
import numpy as np

import tkinter as tk
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

Pregnancies = tk.Entry (root) 
canvas1.create_window(220, 20, window=Pregnancies)
label1 = tk.Label(root, text= 'Pregnancies')
canvas1.create_window(100, 20, window=label1)

Glucose = tk.Entry (root) 
canvas1.create_window(220, 40, window=Glucose)
label1 = tk.Label(root, text= 'Glucose')
canvas1.create_window(100, 40, window=label1)

Blood_Pressure = tk.Entry (root) 
canvas1.create_window(220, 60, window=Blood_Pressure)
label1 = tk.Label(root, text= 'Blood Pressure')
canvas1.create_window(100, 60, window=label1)


Insulin = tk.Entry (root) 
canvas1.create_window(220, 80, window=Insulin)
label1 = tk.Label(root, text= 'Insulin')
canvas1.create_window(100, 80, window=label1)

BMI = tk.Entry (root) 
canvas1.create_window(220, 100, window=BMI)
label1 = tk.Label(root, text= 'BMI')
canvas1.create_window(100, 100, window=label1)

PedigreeFunc = tk.Entry (root) 
canvas1.create_window(220, 120, window=PedigreeFunc)
label1 = tk.Label(root, text= 'PedigreeFunc')
canvas1.create_window(100, 120, window=label1)

Age = tk.Entry (root) 
canvas1.create_window(220, 140, window=Age)
label1 = tk.Label(root, text= 'Age')
canvas1.create_window(100, 140, window=label1)


#########################################################
diabetes = pd.read_csv("~/anaconda3/diabetes.csv")
diabetes_x = DataFrame(diabetes,columns=['Pregnancies','Glucose','BloodPressure','Insulin','BMI','DiabetesPedigreeFunction', 'Age' ])
diabetes_y = DataFrame(diabetes,columns=['Outcome'])

# Split the data into training/testing sets
diabetes_x_train = diabetes_x[:-50]
diabetes_x_test = diabetes_x[-50:-1]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-50]
diabetes_y_test = diabetes_y[-50:-1]

regr = linear_model.LinearRegression()
regr.fit(diabetes_x_train, diabetes_y_train)




def test_function ():  
    pregnancies = Pregnancies.get()
    glucose = Glucose.get()
    blood_pressure = Blood_Pressure.get()
    insulin = Insulin.get()
    bmi = BMI.get()
    pedigreeFunc = PedigreeFunc.get()
    age = Age.get()
    
    
    data= {'Pregnancies': [pregnancies] ,
       'Glucose': [glucose],
       'BloodPressure': [blood_pressure],
       'Insulin': [insulin],
       'BMI': [bmi],
       'DiabetesPedigreeFunction': [pedigreeFunc],
       'Age': [age] }
    diabetes_x_test_custom= DataFrame(data)
    df2 = regr.predict(diabetes_x_test_custom);
    if (df2>.5):
        label1 = tk.Label(root, text= "Positive")
        canvas1.create_window(200, 230, window=label1)
    else: 
        label1 = tk.Label(root, text= "Negative")
        canvas1.create_window(200, 230, window=label1)
    
    #label1 = tk.Label(root, text= df2)
    #canvas1.create_window(200, 230, window=label1)
    
button1 = tk.Button(text='Resut', command=test_function)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
