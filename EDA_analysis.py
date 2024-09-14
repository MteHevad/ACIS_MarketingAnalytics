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

# Machine Learning: Random Forest Classifier
X = pd.get_dummies(df[['Province', 'Gender']], drop_first=True)
y = df['Claimed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

y_pred = rf_model.predict(X_test_scaled)

print("\
Random Forest Classifier Results:")
print(classification_report(y_test, y_pred))

# Feature importance
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': rf_model.feature_importances_})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print("\
Feature Importance:")
print(feature_importance)

# Save results
with open('analysis_results.txt', 'w') as f:
    f.write("Chi-square test results:\
")
    f.write(f"Chi-square statistic: {chi2}\
")
    f.write(f"p-value: {p_value}\
\
")
    f.write("Random Forest Classifier Results:\
")
    f.write(classification_report(y_test, y_pred))
    f.write("\
Feature Importance:\
")
    f.write(feature_importance.to_string())

print("Analysis completed. Results saved in 'analysis_results.txt' and 'claims_distribution.png'.")

# Load the data
df = pd.read_csv('C:/Users/hp/Desktop/KAIM/Week 3/insurance_data.csv')

# 1. Claim rates by province and gender
claim_rates = df.groupby(['Province', 'Gender'])['Claimed'].mean().unstack()
print("Claim rates by province and gender:")
print(claim_rates)

# 2. Visualize the distribution of claims
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Province', hue='Claimed')
plt.title('Distribution of Claims by Province')
plt.savefig('claims_distribution.png')
plt.close()

# 3. Chi-square test for independence
contingency_table = pd.crosstab(df['Province'], df['Claimed'])
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"\
Chi-square test p-value: {p_value:.4f}")

# 4. Simple predictive model (Logistic Regression)
# Encode categorical variables
le = LabelEncoder()
df['Province_encoded'] = le.fit_transform(df['Province'])
df['Gender_encoded'] = le.fit_transform(df['Gender'])

X = df[['Province_encoded', 'Gender_encoded']]
y = df['Claimed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\
Logistic Regression Model Accuracy: {accuracy:.2f}")

# Feature importance
feature_importance = pd.DataFrame({
    'Feature': ['Province', 'Gender'],
    'Importance': abs(model.coef_[0])
})
feature_importance = feature_importance.sort_values('Importance', ascending=False)
print("\
Feature Importance:")
print(feature_importance)

# Convert 'Claimed' to numeric (it should already be, but just in case)
df['Claimed'] = pd.to_numeric(df['Claimed'], errors='coerce')

# Create dummy variables for 'Province' and 'Gender'
df_encoded = pd.get_dummies(df, columns=['Province', 'Gender'])

# Calculate correlation matrix
correlation_matrix = df_encoded.corr()

# Heatmap for correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

print("Correlation analysis completed.")

# Calculate claim rates by province
claim_rates = df.groupby('Province')['Claimed'].mean().sort_values(ascending=False)

# Create a bar plot of claim rates by province
plt.figure(figsize=(10, 6))
claim_rates.plot(kind='bar')
plt.title('Insurance Claim Rates by Province')
plt.xlabel('Province')
plt.ylabel('Claim Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Claim rates by province:")
print(claim_rates)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Province', y='Claimed', data=df)
plt.title('Distribution of Claims by Province')
plt.xlabel('Province')
plt.ylabel('Claimed Amount')
plt.show()

print("Box plot of claims by province created.")
