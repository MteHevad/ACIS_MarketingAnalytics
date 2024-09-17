# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = 'C:\Users\hp\Desktop\KAIM\Week 3\insurance_data.csv'  # Update with the actual dataset path
data = pd.read_csv(data_path)

# Task: Define KPIs
# We will use risk (e.g., Claim rate) and margin (profit) as the key performance indicators (KPIs)
kpi_risk = 'Claimed'  # This is the risk metric
kpi_margin = 'Profit'  # This is the profit metric (hypothetically)

# Data Segmentation
# Split data into groups for A/B testing
# For provinces and zip codes, create two groups: A (Control) and B (Test) using dummy segmentation
group_a = data[data['Province'] == 'Province_A']  # Control group: Province A
group_b = data[data['Province'] == 'Province_B']  # Test group: Province B

# Null Hypothesis 1: No risk differences across provinces
# Perform a chi-squared test for categorical variable 'Claimed' across provinces
observed_province = pd.crosstab(data['Province'], data[kpi_risk])
chi2_province, p_province, _, _ = stats.chi2_contingency(observed_province)

# Print results for provinces
print(f"Chi-squared test for Province and Risk (Claim Rate):")
print(f"p-value: {p_province}")
if p_province < 0.05:
    print("Reject the null hypothesis: There are significant risk differences across provinces.")
else:
    print("Fail to reject the null hypothesis: No significant risk differences across provinces.\n")

# Null Hypothesis 2: No risk differences between zip codes
# Perform a chi-squared test for 'Claimed' between zip codes
observed_zip = pd.crosstab(data['ZipCode'], data[kpi_risk])
chi2_zip, p_zip, _, _ = stats.chi2_contingency(observed_zip)

# Print results for zip codes
print(f"Chi-squared test for Zip Code and Risk (Claim Rate):")
print(f"p-value: {p_zip}")
if p_zip < 0.05:
    print("Reject the null hypothesis: There are significant risk differences between zip codes.")
else:
    print("Fail to reject the null hypothesis: No significant risk differences between zip codes.\n")

# Null Hypothesis 3: No significant margin differences between zip codes
# Perform a t-test for numerical data (e.g., 'Profit' between zip codes)
group_a_profit = group_a[kpi_margin].dropna()  # Group A (control)
group_b_profit = group_b[kpi_margin].dropna()  # Group B (test)
t_stat_zip, p_profit_zip = stats.ttest_ind(group_a_profit, group_b_profit)

# Print results for profit differences between zip codes
print(f"T-test for Zip Code and Profit (Margin):")
print(f"p-value: {p_profit_zip}")
if p_profit_zip < 0.05:
    print("Reject the null hypothesis: There are significant margin differences between zip codes.")
else:
    print("Fail to reject the null hypothesis: No significant margin differences between zip codes.\n")

# Null Hypothesis 4: No significant risk difference between men and women
# Perform a chi-squared test for 'Claimed' between gender groups
observed_gender = pd.crosstab(data['Gender'], data[kpi_risk])
chi2_gender, p_gender, _, _ = stats.chi2_contingency(observed_gender)

# Print results for gender differences
print(f"Chi-squared test for Gender and Risk (Claim Rate):")
print(f"p-value: {p_gender}")
if p_gender < 0.05:
    print("Reject the null hypothesis: There are significant risk differences between men and women.")
else:
    print("Fail to reject the null hypothesis: No significant risk differences between men and women.\n")

# Visualizing Risk Across Provinces and Gender
# Risk by Province (Claim Rate)
plt.figure(figsize=(8, 5))
sns.barplot(x='Province', y=kpi_risk, data=data, estimator=np.mean)
plt.title('Risk (Claim Rate) by Province')
plt.ylabel('Average Claim Rate')
plt.show()

# Risk by Gender
plt.figure(figsize=(8, 5))
sns.barplot(x='Gender', y=kpi_risk, data=data, estimator=np.mean)
plt.title('Risk (Claim Rate) by Gender')
plt.ylabel('Average Claim Rate')
plt.show()

# Summary: Analyze and Report
# The printed output above provides the statistical outcomes and p-values for each hypothesis.

