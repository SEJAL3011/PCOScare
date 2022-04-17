
import numpy as np #create arrays
import pandas.util.testing as tm
import pandas as pd
import matplotlib.pyplot as plt #plot data
import seaborn as sns #plot data
import missingno as ms #plot missing data

df = pd.read_csv('https://hiyabose/hackout-app/master/pcos.csv?token=AMDBGXCLZMVYM53W756SYXK7V3JFW', sep=',' , encoding='latin-1')

df.info()

df[[' Age (yrs)','Blood Group','Cycle length(days)','PCOS (Y/N)','Cycle(months)','Bloated','facial hair','chest hair','difficult to loose weight','mood swings','anxiety/depression/stress','Irregular_sleep','Fast food (Y/N)','Pregnant(Y/N)','No of aborptions','Hip(inch)','Waist(inch)','Weight gain(Y/N)','hair growth(Y/N)','Skin darkening (Y/N)','Hair loss(Y/N)','Pimples(Y/N)','Reg Exercise(Y/N)']] = df[[' Age (yrs)','Blood Group','Cycle length(days)','PCOS (Y/N)','Cycle(months)','Bloated','facial hair','chest hair','difficult to loose weight','mood swings','anxiety/depression/stress','Irregular_sleep','Fast food (Y/N)','Pregnant(Y/N)','No of aborptions','Hip(inch)','Waist(inch)','Weight gain(Y/N)','hair growth(Y/N)','Skin darkening (Y/N)','Hair loss(Y/N)','Pimples(Y/N)','Reg Exercise(Y/N)']].astype(float)

df.info()

from sklearn import svm

from sklearn.model_selection import train_test_split

train = df.drop(['Sl No','Patient File No','PCOS (Y/N)','Pulse rate(bpm) '], axis=1)
train= np.asarray(train, dtype='float64')
test = df['PCOS (Y/N)']
test= np.asarray(test, dtype='float64')

test.shape

X_train, X_test, y_train, y_test = train_test_split(train,test, test_size=0.2, random_state=2)

clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

y_train.shape,y_test.shape



pred

reg.score(X_test, y_test)



X_test.shape

x=[[28,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,44,152,19.3,15,78,1,5,7,36,30,0.83333]]

o = reg.predict(x)
print (o)

import pickle
pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))