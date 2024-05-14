from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

def upload(request):
    return render(request,'upload.html')

def result(request):
    data= pd.read_csv(r'C:/Users/Harikrishna/Desktop/dataset/diabetes.csv')
    
    x= data.drop('Outcome', axis=1)
    y=data['Outcome'] 
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    
    model= LogisticRegression()
    model.fit(x_train,y_train)
    
    val1=float(request.GET['Pregnancies'])
    val2=float(request.GET['glucose'])
    val3=float(request.GET['pressure'])
    val4=float(request.GET['skin_thickness'])
    val5=float(request.GET['Insulin'])
    val6=float(request.GET['bmi'])
    val7=float(request.GET['Diabetes_Pedigree'])
    val8=float(request.GET['age'])
    
    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    
    result1=" "
    if pred==[1]:
        result1="Oops! You have DIABETES"
    else:
        result1="Great! You DON'T have diabetes"    
    
    return render(request,'predict.html',{"result2":result1})