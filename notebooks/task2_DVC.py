import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the provided path
file_path = r'C:\Users\hp\Desktop\KAIM\Week 3\insurance_data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data to verify successful loading
print(data.head())

# Print available columns to verify the presence of 'TotalPremium' or similar
print("Available columns:", data.columns)

# Strip any leading or trailing spaces from column names
data.columns = data.columns.str.strip()

# Check if 'TotalPremium' exists or find similar column names
if 'TotalPremium' in data.columns:
    print("'TotalPremium' column is present.")
else:
    # Search for columns containing 'Premium' and suggest alternatives
    premium_columns = [col for col in data.columns if 'Premium' in col]
    print(f"Did you mean one of these columns? {premium_columns}")

# Selecting only numerical columns for descriptive statistics and filling missing values
numerical_columns = data.select_dtypes(include=[np.number]).columns

# Variability of numerical features (e.g., 'TotalPremium' and 'TotalClaims')
if 'TotalPremium' in numerical_columns:
    total_premium_var = data['TotalPremium'].var()
    print(f"Variance of TotalPremium: {total_premium_var}")

if 'TotalClaims' in numerical_columns:
    total_claims_var = data['TotalClaims'].var()
    print(f"Variance of TotalClaims: {total_claims_var}")

# Summary statistics for all numerical columns
summary_stats = data[numerical_columns].describe()
print("Summary Statistics for numerical columns:\n", summary_stats)

# Fill missing values for numerical columns only using the median
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].median())

# Display missing values after imputation
missing_values_after = data.isnull().sum()
print("Missing Values after filling numerical columns:\n", missing_values_after)

# Plotting histograms for numerical columns
for col in numerical_columns:
    if col in data.columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[col], bins=30, kde=True)
        plt.title(f'Histogram of {col}')
        plt.show()

# Plotting bar charts for categorical columns
categorical_columns = data.select_dtypes(include=['object']).columns  # Extract only categorical columns
for col in categorical_columns:
    if col in data.columns:
        plt.figure(figsize=(8, 6))
        sns.countplot(x=col, data=data)
        plt.title(f'Countplot of {col}')
        plt.show()

# Scatter plot and correlation matrix for 'TotalPremium' vs 'TotalClaims' by PostalCode
if 'TotalPremium' in numerical_columns and 'TotalClaims' in numerical_columns and 'PostalCode' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='TotalPremium', y='TotalClaims', hue='PostalCode', data=data)
    plt.title('TotalPremium vs TotalClaims by PostalCode')
    plt.show()

# Correlation matrix for numerical columns
correlation_matrix = data[numerical_columns].corr()
print("Correlation Matrix:\n", correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Box plots to detect outliers in numerical data
for col in numerical_columns:
    if col in data.columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(data[col])
        plt.title(f'Boxplot of {col}')
        plt.show()

# Pairplot for numerical features only
sns.pairplot(data[numerical_columns])
