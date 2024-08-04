import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from matplotlib import pyplot as plt



data = pd.read_csv('projects/renewable_energy.csv')
data.drop(columns=['Flag Codes'],inplace=True)
data.fillna({'Value':data['Value'].mean()},inplace=True)

# features

numerical = ['TIME']
categorical = ['LOCATION','INDICATOR','SUBJECT','MEASURE','FREQUENCY']



# transformers

numerical_transformer = SimpleImputer(strategy="mean")
categorical_transformer = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='constant',fill_value='missing')),
        ('onehot',OneHotEncoder(handle_unknown='ignore'))
    ]
    
)

# preprocessor

preprocessor = ColumnTransformer(
    transformers=[
        ('num',numerical_transformer,numerical),
        ('cat',categorical_transformer,categorical)
    ]
)

# model

model = Pipeline(
    steps=[
        ('preprocessor',preprocessor),
        ('regressor',LinearRegression())
    ]
)

features = ['LOCATION','INDICATOR','SUBJECT','MEASURE','FREQUENCY','TIME']
target = 'Value'

x = data[features]
y = data[target]


x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.9,test_size=0.1)

if len(x_train.shape) < 2:
    x_train = np.array(x_train).reshape(-1,1)
    x_test = np.array(x_test).reshape(-1,1)


# Model fiting
model.fit(x_train,y_train)

to_predict = pd.DataFrame([["TGO","RENEWABLE","TOT","KTOE","A",1970]],columns=features)

# Make a prediction
y_pred = model.predict(x_test)

# Print results
print("Prediction:", y_pred)
print("Train score:", model.score(x_train, y_train))
print("Test score:", model.score(x_test, y_test))

# Plotting
plt.scatter(x_test['TIME'], y_test, color='blue', label='Expected data in testing')
plt.plot(x_test['TIME'],y_pred,'ro',label="Prediction")
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()


