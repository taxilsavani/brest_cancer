# -*- coding: utf-8 -*-
"""Assignment2-BreastCancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vWbr4aA2bWUBJnyXYuZE-Rx4f4rjXgny
"""

import pandas as pd
import numpy as np

data=pd.read_csv('data.csv')

data.head()

data.describe()

data.isna().sum()

x=data.drop('Classification',axis=1)
y=data['Classification']

x.head()

y.head()

y

#splitting to the train and test data for both dataset "Data", "Data2"
from sklearn.model_selection import train_test_split
x_train,x_validate,y_train,y_validate = train_test_split(x,y, test_size=0.20,random_state=0, stratify=y)

#Importing decision tree for sklearn liabrary
from sklearn.tree import DecisionTreeClassifier
dc = DecisionTreeClassifier()
#fitting the model with the training data
dc.fit(x_train,y_train)

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
y_predict=dc.predict(x_validate)
acu=accuracy_score(y_validate,y_predict)
acu

import pickle
filename = 'Taxil_DTmodel_v1.sav'
pickle.dump(dc, open(filename, 'wb'))

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train,y_train)

y_predict=gnb.predict(x_validate)
acu=accuracy_score(y_validate,y_predict)
acu

from sklearn.metrics import classification_report
print(classification_report(y_validate,y_predict))

filename = 'Taxil_GNBmodel_v1.sav'
pickle.dump(dc, open(filename, 'wb'))