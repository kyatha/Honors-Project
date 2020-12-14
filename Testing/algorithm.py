import numpy as np
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import pickle


#read the training dataset
df = pd.read_csv('all_appliances.csv')

#Spliting the dataset in independent and dependent variables
X = df.iloc[:,:5].values
Y = df.iloc[:,5:8].values

# Splitting the dataset into the Training set and Test set
features_train, features_test, labels_train, labels_test = train_test_split (X, Y, test_size=0.20, random_state=0)


# Feature Scaling to bring the variable in a single scale
# scaler = StandardScaler()
# X_train = scaler.fit_transform(features_train)
# X_test = scaler.transform(features_test)

#model
clf = KNeighborsClassifier(n_neighbors=3)

#train
clf.fit(features_train, labels_train)

#test
y_pred = clf.predict(features_test)
print(y_pred)

#accuracy
acc = accuracy_score(y_pred, labels_test)
print(acc)

#Pickle
file_name = 'knn_algo'
outfile = open(file_name,'wb')
pickle.dump(clf,outfile)
outfile.close()


