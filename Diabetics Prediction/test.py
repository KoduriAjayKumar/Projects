#Python 3.7.8
#numpy==1.21.6
#keras==2.11.0
#tensorflow==2.11.0
#joblib==1.2.0


#Project: Diabetics - Detection for Women

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


from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import joblib

data = loadtxt("pima-indians-diabetes.csv",delimiter = ',')
X = data[ : , 0: 8]  
y = data[:,8]

model = joblib.load("modelSeq.sav")
print("Loaded  model from disk")

predictions = model.predict(X)>0.5
for i in range(10,15):
    print("%s => %d ( Original Class: %d)" % (X[i].tolist(),predictions[i],y[i] ))


    
