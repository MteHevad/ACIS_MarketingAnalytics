# preprocessing_pipeline.py
from scripts.data_cleaning import clean_data
from scripts.feature_engineering import feature_engineering
import pandas as pd

def preprocess_data(file_path):
    # Load data
    data = pd.read_csv(file_path)

    # Data cleaning
    data = clean_data(data)

    # Feature engineering
    data = feature_engineering(data)

    return data
