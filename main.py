#IMPORTING LIBRARIES
import random
import pandas as pd
import numpy as np
import xlsxwriter


#################################################
def normalize(prediction):

    i = 0;
    while i < 197:
        prediction.append( ((prediction[i] - min(prediction)) / ( max(prediction) - min(prediction)))* 1);
        i = i + 1
    return prediction
#################################################
def updateParametrs(predictions,targets,weights,bias,data):
  i = 0;
  j = 0;
  k = 0;
  learning_rate = 0.1; # setting learning rate at 0.1
  temp = list();
  sums =0;
  updatedWeight = list();
  while i < 9503:
    while j < 197:

       temp.append((-(targets[j] - predictions[j]))*data[j][i])
       j = j + 1
       #end
    updatedWeight.append(weights[i] - (learning_rate*np.sum(temp)));
    j = 0;
    temp.clear();
    i = i+1
  return updatedWeight
################################################


#READING EXCEL DATA FROM EXCEL FILE
path = 'file.xlsx'; # PATH TO THE FEATURE FILE
df = pd.read_excel(path); # READING THE EXCEL FILE
data = df.to_numpy(); # CONVERTING DATA FRAME TO NUMPY ARRAY
#-------------------------------------------------------
targets = list();
i = 0;
while i < 197:
     targets.append(data[i][9504]);
     i = i + 1
#-------------------------------------------------------
# INTALIZING WEIGHTS WITH RANDOM VALUE BETWEEN 0-1
weights = list();
i =0;
while i < 9503:
    weights.append( random.uniform(0.1,0.9));
    i = i+1;
#-------------------------------------------------------
# NORMALIZING TARGET VALUE FROM 1 - 200 INTO 0 - 1
i = 0
while i < 197:
    print(data[i][9504])
    data[i][9504] = ((1 -data[i][9504])/(1-200)) * 1
    i = i+1;
#-------------------------------------------------------
bias = 0.3;
prediction = list();
k = 0;
while k < 100: # updating parameter 100 times
# prediction calculation
    i = 0;
    j = 0;
    sum = 0;
    while i < 197:
        while j < 9503:
                sum =sum + data[i][j]*weights[j];
                j = j + 1
        j = 0;
        prediction.append(sum);
        sum =0;
        i = i + 1;
     # prediction calculation
    #updating parameters
    prediction = normalize(prediction)
    weights = updateParametrs(prediction,targets,weights,bias,data);
    print("UPDATED WEIGHTS ARE",weights)
    k = k +1

print("FINAL WEIGHTS AFTER 100 ITERATIONS ARE",weights)
df = pd.DataFrame(weights)
writer = pd.ExcelWriter('model.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=True)
writer.save()










