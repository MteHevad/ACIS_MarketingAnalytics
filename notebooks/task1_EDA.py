# EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_path = "C:/Users/hp/Desktop/KAIM/Week 3/insurance_data.csv"
data = pd.read_csv(data_path)

# Basic data summary
print(data.describe())
print(data.info())

# Missing values
missing_values = data.isnull().sum()
print(missing_values)

# Histograms for numerical columns
data.hist(bins=50, figsize=(20, 15))
plt.show()

# Correlation matrix
corr_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.show()

