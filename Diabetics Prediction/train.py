#Python 3.7.8
#numpy==1.21.6
#keras==2.11.0
#tensorflow==2.11.0
#joblib==1.2.0


'''Project: Diabetics - Detection for Women
 In this project we use a pima-indians-diabetes dataset to train a machine learning model to predict whether a woman has diabetes
 based on various input features. we use this dataset to train  neural network model, evaluate its accuracy and save the model for future use.
 The saved model can be loaded later to make predictions on new data.
'''
'''
   1. Number of times pregnant
   2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
   3. Diastolic blood pressure (mm Hg)
   4. Triceps skin fold thickness (mm)
   5. 2-Hour serum insulin (mu U/ml)
   6. Body mass index (weight in kg/(height in m)^2)
   7. Diabetes pedigree function
   8. Age (years)
   9. Class variable (0 or 1)
'''

from numpy import loadtxt  #handle/load dataset
from keras.models import Sequential  #Empty working area
from keras.layers import Dense  #Dense layer 
import joblib

data = loadtxt("pima-indians-diabetes.csv",delimiter = ',')

X = data[ : , 0: 8]  #Numpy arrays - Feautres
y = data[:,8]                       #Labels-output

#print(X.shape)
#print(y.shape)

model = Sequential()
model.add(Dense(12,input_dim = 8,activation = 'relu'))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation = "sigmoid"))

model.compile(loss = "binary_crossentropy",optimizer="adam",metrics=["accuracy"])
model.fit(X,y,epochs=5,batch_size=10)

accuracy = model.evaluate(X,y)
print("Accuracy = %.2f"%(accuracy[1]))

#To save model in current local directory
joblib.dump( model, "modelSeq.sav")


