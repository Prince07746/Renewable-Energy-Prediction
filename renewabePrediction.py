import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from matplotlib import pyplot as plt

# Load the data
data = pd.read_csv('renewable_energy.csv')

# Drop the 'Flag Codes' column as it's not needed for the model
data.drop(columns=['Flag Codes'], inplace=True)

# Fill missing 'Value' column with the mean of the column
data.fillna({'Value': data['Value'].mean()}, inplace=True)

# Define features
numerical = ['TIME']
categorical = ['LOCATION', 'INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY']

# Define transformers for numerical and categorical data
numerical_transformer = SimpleImputer(strategy="mean")

categorical_transformer = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),  # Fill missing values with 'missing'
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categorical variables
    ]
)

# Preprocessor to apply transformations to the correct columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical),  # Apply numerical transformer to numerical columns
        ('cat', categorical_transformer, categorical)  # Apply categorical transformer to categorical columns
    ]
)

# Define the model pipeline
model = Pipeline(
    steps=[
        ('preprocessor', preprocessor),  # Preprocess the data
        ('regressor', LinearRegression())  # Apply linear regression
    ]
)

# Separate features and target variable from the data
features = ['LOCATION', 'INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY', 'TIME']
target = 'Value'

x = data[features]
y = data[target]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, test_size=0.1)

# Reshape data if necessary (for compatibility with certain models)
if len(x_train.shape) < 2:
    x_train = np.array(x_train).reshape(-1, 1)
    x_test = np.array(x_test).reshape(-1, 1)

# Fit the model to the training data
model.fit(x_train, y_train)

# Prepare data for prediction
to_predict = pd.DataFrame([["TGO", "RENEWABLE", "TOT", "KTOE", "A", 1970]], columns=features)

# Make predictions on the test data
y_pred = model.predict(x_test)

# Print results
print("Prediction:", y_pred)
print("Train score:", model.score(x_train, y_train))
print("Test score:", model.score(x_test, y_test))

# Plotting results
plt.scatter(x_test['TIME'], y_test, color='blue', label='Expected data in testing')
plt.plot(x_test['TIME'], y_pred, 'ro', label="Prediction")
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
