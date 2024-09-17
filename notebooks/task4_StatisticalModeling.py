# Import necessary libraries 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import shap

# Load the dataset
data_path = r'C:\Users\hp\Desktop\KAIM\Week 3\insurance_data.csv'
insurance_data = pd.read_csv(data_path)

# Data Preparation
# Fill missing values for numeric columns using the median
numeric_columns = insurance_data.select_dtypes(include=[np.number]).columns
insurance_data[numeric_columns] = insurance_data[numeric_columns].fillna(insurance_data[numeric_columns].median())

# Fill missing values for categorical columns using the mode (most frequent value)
categorical_columns = insurance_data.select_dtypes(include=[object]).columns
insurance_data[categorical_columns] = insurance_data[categorical_columns].fillna(insurance_data[categorical_columns].mode().iloc[0])

# Encoding Categorical Data: Use one-hot encoding for categorical variables like 'Province' and 'Gender'
insurance_data = pd.get_dummies(insurance_data, columns=['Province', 'Gender'], drop_first=True)

# Feature Selection: Select relevant features for predicting 'Claimed'
features = insurance_data.drop(columns=['Claimed'])  # All features except the target 'Claimed'
target = 'Claimed'

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(features, insurance_data[target], test_size=0.3, random_state=42)

# Modeling Techniques
# 1. Logistic Regression
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)

# 2. Random Forest Classifier
rf_clf = RandomForestClassifier(random_state=42)
rf_clf.fit(X_train, y_train)
y_pred_rf = rf_clf.predict(X_test)

# 3. XGBoost Classifier
xgb_clf = xgb.XGBClassifier(objective='binary:logistic', random_state=42)
xgb_clf.fit(X_train, y_train)
y_pred_xgb = xgb_clf.predict(X_test)

# Model Evaluation Function
def evaluate_model(y_test, y_pred, model_name):
    print(f"{model_name} Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")
    print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")
    print("\n")

# Evaluate all models
evaluate_model(y_test, y_pred_log, "Logistic Regression")
evaluate_model(y_test, y_pred_rf, "Random Forest")
evaluate_model(y_test, y_pred_xgb, "XGBoost")

# Feature Importance Analysis (SHAP)
# SHAP works better with Tree-based models, so we use XGBoost for SHAP analysis
explainer = shap.Explainer(xgb_clf, X_test)
shap_values = explainer(X_test)

# SHAP summary plot
shap.summary_plot(shap_values, X_test)

# SHAP dependence plot for one of the important features, e.g., 'Province_C' after one-hot encoding
shap.dependence_plot('Province_C', shap_values, X_test)
