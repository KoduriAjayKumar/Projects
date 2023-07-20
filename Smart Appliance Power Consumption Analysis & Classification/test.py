#Python 3.7.8
#scikit-learn==1.0.2
#joblib==1.2.0
#pandas==1.3.5

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

#split data into training data set and test data set
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 1)

#To load model:
model = joblib.load("modelSVM.sav")
print(model)


predictions = model.predict(X_test)
accuracy = accuracy_score( y_test, predictions )
print("Predictions : ",predictions)
print("Actual Class : ",y_test)
print("accuracy : ", accuracy )
