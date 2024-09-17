# data_cleaning.py
import pandas as pd

def clean_data(data):
    # Drop columns with too many missing values
    data = data.dropna(thresh=0.7*len(data), axis=1)

    # Impute remaining missing values
    data.fillna(data.median(), inplace=True)

    # Drop duplicates
    data.drop_duplicates(inplace=True)

    return data
