# -*- coding: utf-8 -*-
"""SMD.ipynb


Original file is located at
    https://colab.research.google.com/drive/1EJ6AZ4_mKfjNN6dwW0JERDbU1WFY089M
"""

!pip install pgmpy

"""**Required Libraries**"""

#Libraries required for the project
import pandas as pd #for reading the dataset(csv) file to implement the code
from pgmpy.models import BayesianModel #from pgmpy importing the naive bayes model
from pgmpy.estimators import MaximumLikelihoodEstimator #importing the maxLikelyhood Estimater
from pgmpy.inference import VariableElimination #importing the VariableElimination module

"""**Data Loading and Preprocessing**"""

data=pd.read_csv("ai_spam_dataset_500.csv") #using pandas we read the dataset
Spam_or_Ham=pd.DataFrame(data) #converting the dataset to a data frame

data.head() #the first four values of the dataset to know the format

print(Spam_or_Ham) #Printing the data frame that is being loaded to the model

import seaborn as sns

sns.countplot(x="frequency_of_words",hue="spam",data=data)

"""MODEL"""

naive_bayes_model = BayesianModel([ #using the naive bayes model to find the relation and build the model
    ('frequency_of_words','spam') #the is a definite relation between the frequency of words and a mail being spam or ham
])

naive_bayes_model.fit(Spam_or_Ham, estimator=MaximumLikelihoodEstimator) #Using the model.fit() to train the model with dataframe

Bayes_SMD = VariableElimination(naive_bayes_model)# the VariableElimination model is used to perform inference

"""**MODEL** **TESTING**"""

def Count(m):#this method is used to count the frequency words
  d = {"the":0,"of":0,"a":0,"an":0,"by":0,"to":0,"ect":0,"and":0,"for":0,"you":0,"at":0}
  for i in m.split():
    if i.lower() in d:
      d[i.lower()]+=1
  s = 0
  for i in d:
    s+=d[i]
  return s

def TestTheModel(): #this method is used to test the model with a mail data to check whether it is spam or ham
  mail_data = input()
  value = Count(mail_data)
  q = Bayes_SMD.query(variables=['spam'],evidence={
    'frequency_of_words': int(value)
  })
  print("==========================================")
  print("==========================================")
  if q.values[1]==1:
    print("            It is a Spam Mail           ")
  else:
    print("            It is a Ham Mail          ")
  print("==========================================")
  print("==========================================")

TestTheModel() #Final function call