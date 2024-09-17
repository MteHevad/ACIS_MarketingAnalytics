# feature_engineering.py
import pandas as pd

def feature_engineering(data):
    # Feature extraction for TotalPremium and TotalClaims
    data['Claim_Premium_Ratio'] = data['TotalClaims'] / (data['TotalPremium'] + 1)

    # Creating dummy variables for categorical columns
    data = pd.get_dummies(data, drop_first=True)

    return data
