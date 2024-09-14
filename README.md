# ACIS Marketing Analytics Project
# Weekly Project - Data Version Control (DVC) and Git Versioning

## Overview

This project demonstrates the use of Git, GitHub, and DVC for version control and managing machine learning workflows with a focus on data versioning. The project also includes Exploratory Data Analysis (EDA) and statistical analysis on insurance datasets. The work is organized into two tasks:

- **Task 1: Git, GitHub, and Exploratory Data Analysis**
- **Task 2: Data Version Control (DVC)**

---

## Task 1: Git and GitHub with Exploratory Data Analysis (EDA)

### Objectives:
1. **Git Version Control:** 
   - Create a GitHub repository to host the project code and data.
   - Set up continuous integration (CI) with GitHub Actions.
   
2. **Exploratory Data Analysis (EDA):**
   - Understand the dataset, summarize it, and detect patterns.
   - Apply statistical thinking to discover actionable insights.

### Steps:
1. **Git Repository Setup:**
   - Initialize a Git repository for the project.
   - Create branches for different tasks (e.g., `task-1` for EDA).
   - Commit changes to the repository at least three times a day with descriptive commit messages.

2. **EDA Process:**
   - **Data Summarization:** Calculate descriptive statistics (e.g., variability of numerical features like `TotalPremium`, `TotalClaim`).
   - **Data Structure:** Review the data types and format categorical variables and dates.
   - **Data Quality Assessment:** Handle missing values, identify and deal with outliers.
   - **Univariate and Bivariate Analysis:** 
     - Analyze the distribution of individual variables using histograms for numerical and bar charts for categorical data.
     - Analyze relationships between variables such as `TotalPremium` and `TotalClaims` using scatter plots and correlation matrices.
   - **Outlier Detection:** Detect outliers using box plots.
   - **Visualization:** Produce at least 3 insightful plots to visually capture key insights.

### KPIs:
- Demonstrate a clear understanding of Git version control.
- Show creativity and statistical understanding in EDA, including trends, correlations, and outlier detection.
- Proactively learn and use advanced EDA techniques.

---

## Task 2: Data Version Control (DVC)

### Objectives:
1. Set up DVC for managing dataset versions.
2. Use Git for version control of code and DVC metadata.
3. Push the versioned data to local remote storage.

### Steps:
1. **Install DVC:**
   - Install DVC using pip: `pip install dvc`.

2. **Initialize DVC in the Project Directory:**
   - Navigate to the project directory and run `dvc init` to initialize DVC.

3. **Set Up Local Remote Storage:**
   - Create a storage directory for versioned datasets.
   - Add the storage directory as a DVC remote using the command: 
     ```bash
     dvc remote add -d localstorage /path/to/your/local/storage
     ```

4. **Add Data to DVC:**
   - Use DVC to track the dataset with `dvc add data.csv`.
   - Commit the changes to Git.

5. **Version Control:**
   - Commit the `.dvc` files to the Git repository, ensuring each version of the dataset is tracked.

6. **Push Data to Remote:**
   - Push the data to the local remote storage using `dvc push`.

7. **Branching and Merging:**
   - Merge branches from task-1 into the main branch using Pull Requests (PR).
   - Create a new branch for task-2 (`task-2`), commit all DVC-related work, and push to the GitHub repository.

### KPIs:
- Successfully install and configure DVC.
- Version control datasets using DVC and push them to local remote storage.
- Commit and push DVC metadata files to GitHub.
  
---
