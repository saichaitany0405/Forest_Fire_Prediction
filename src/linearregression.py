import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_inline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

df = pd.read_csv('datasets/Algerian_forest_fires_dataset_UPDATE.csv', header=1)
# print(df.head())
# print(df.isnull().sum())
# print(df[df.isnull().any(axis=1)])
df.loc[:122,'region']=0
df.loc[122:,'region']=1
df['region']=df['region'].astype(int)
df =df.dropna().reset_index(drop=True)
# print(df.isnull().sum())
df= df.drop(122).reset_index(drop=True)
# print(df.loc[122])
df.columns=df.columns.str.strip()
# print(df.columns)
df[['day','month','year','Temperature','RH','Ws']] = df[['day','month','year','Temperature','RH','Ws']].astype(int)
df[['Rain','FFMC','DMC','DC','ISI','BUI','FWI']] = df[['Rain','FFMC','DMC','DC','ISI','BUI','FWI']].astype(float)
# print(df)
df_copy = df.drop(['day','month','year',],axis=1)
df_copy['Classes']=np.where(df_copy['Classes'].str.contains('not fire'),0,1)
df_copy['Classes'].value_counts()
df_copy.to_csv("datasets/cleaned_dataset.csv")
df=df_copy
X=df.drop('FWI',axis=1)
y=df['FWI']

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=.80,random_state=42)
# print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)
scaler= StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled,y_train)
y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
R2 = r2_score(y_test,y_pred)
print(mse,mae,rmse,R2)

import pickle
with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('models/LinearRegression.pkl', 'wb') as f:
    pickle.dump(model, f)



