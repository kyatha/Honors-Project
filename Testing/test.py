import serial
import sys
import os
import time
from sklearn.preprocessing import MultiLabelBinarizer
import pickle
from statistics import mean
from statistics import median
from statistics import stdev
import numpy as np


#unpickle
#file_name = 'knn_algo'
infile = open('knn_algo','rb')
new_algo = pickle.load(infile)
infile.close()

ser = serial.Serial('COM4',9600)
data_list = []

while 1:
    if(ser.in_waiting >0):
        data = ser.readline()
        data_1 = float(data)
        # print(data_1)
        data_list.append(data_1)
        # print(data_list)
        # time.sleep(2)
        if len(data_list) >15:

            feat = data_list[2:15]
            # print(data_list)
            print(feat)
            #create features
            Average_Current = mean(feat)
            # print(Average_Current)
            Max_Current = max(feat)
            # print(Max_Current)
            Min_Current= min(feat)
            # print(Min_Current)
            Median_Current = median(feat)
            #print(Median_Current)
            StDeviation_Current = stdev(feat)
            #print(StDeviation_Current)
            X_test=np.array([Average_Current,Max_Current,Min_Current,Median_Current,StDeviation_Current])
            #print(X_test)
            x_test = X_test.reshape(1, -1)
            y_pred = new_algo.predict(x_test)
            print(y_pred)
            pred_y = y_pred[0].tolist()
            if pred_y== [0,0,0]:
                print('Nothing is connected')
            elif pred_y == [0,0,1]:
                print('Fridge')
            elif pred_y == [1,0,0]:
                print('Coffee Machine')
            elif pred_y == [0,1,0]:
                print('Electric Kettle')
            elif pred_y == [1,1,0]:
                print('Coffee Machine, Electric Kettle')
            elif pred_y == [1,0,1]:
                print('Coffee Machine, Fridge')
            elif pred_y == [0,1,1]:
                print('Electric Kettle,Fridge')
            elif pred_y == [1,1,1]:
                print('Fridge, Electric Kettle, Coffee Machine')
            
            data_list=[]
            #get actual classes
            

      
            





#get actual classes
#mlb = MultiLabelBinarizer()
#actual_appliances = mlb.inverse_transform(y_pred)
#print(actual_appliances)





#get actual classes
#mlb = MultiLabelBinarizer()
#actual_appliances = mlb.inverse_transform(y_pred)
#print(actual_appliances)