import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Load the data
df = pd.read_csv('C:/Users/hp/Desktop/KAIM/Week 3/insurance_data.csv')

# Display basic information about the dataset
print(df.info())

# Display the first few rows of the dataset
print("\
First few rows of the dataset:")
print(df.head())

# Display summary statistics
print("\
Summary statistics:")
print(df.describe())

# Check for missing values
print("\
Missing values:")
print(df.isnull().sum())

print("Data loaded and initial exploration completed.")

# EDA: Visualizations
plt.figure(figsize=(12, 5))

# Claims by Province
plt.subplot(121)
df['Province'].value_counts().plot(kind='bar')
plt.title('Claims by Province')
plt.xlabel('Province')
plt.ylabel('Count')

# Claims by Gender
plt.subplot(122)
df['Gender'].value_counts().plot(kind='bar')
plt.title('Claims by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('claims_distribution.png')
plt.close()

# Hypothesis Testing: Chi-square test for independence
contingency_table = pd.crosstab(df['Province'], df['Claimed'])
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print("Chi-square test results:")
print(f"Chi-square statistic: {chi2}")
print(f"p-value: {p_value}")

