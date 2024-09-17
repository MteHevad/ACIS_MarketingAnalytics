# linear_regression.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_linear_regression(data):
    # Select relevant columns
    X = data.drop(columns=['TotalClaims', 'TotalPremium'])
    y = data['TotalClaims']

    # Train-Test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    print(f"Linear Regression MSE: {mse}")

    return model

