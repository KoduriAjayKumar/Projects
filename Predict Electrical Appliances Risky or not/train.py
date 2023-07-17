#Python 3.7.8
#scikit-learn==1.0.2
#joblib==1.2.0
#pandas==1.3.5

# Machine Learning Classification Algorithm : Support Vector Machine(SVM)
# Prediction of different Electrical Appliances (of Home amd industries) power consumption is risky or not.
# In industries and homes there are lot of Electrical Appliances/Machines, but if we have a problem with certain electrical appliance,
# we don't know the power consumption of that electrical appliance. They monitors all electrical appliances in terms of units.
# But by using M.L. algorithm we can able to classify by analysing different parameters( current, voltage, power) to make decision
# whether the electrical appliance is Risky, Medium, Normal, Noload.
# The data is acquired with the help of Raspberry Pi (series of single-board computers) and current, voltage, power sensors.

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

data = pd.read_csv("Energy Meter.csv")
#print(data.head())
array = data.values

# Create Features and Labels:
X = array[ : , 0:3 ]  #Features
y = array[ : , 3 ]    #Labels

#print(X)
#print(y[1:5])
print(X.shape, y.shape)

#split data into training data set and test data set
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 1)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# Create Model
model = svm.SVC( gamma = 'auto')
model.fit( X_train, y_train )  # Training the model
print(model)

#To save model in current local directory
joblib.dump( model, "modelSVM.sav" )




