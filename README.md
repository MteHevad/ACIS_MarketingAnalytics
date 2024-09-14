# Data Version Control (DVC) Setup

## Overview

This document provides instructions for setting up and using Data Version Control (DVC) in your project to manage dataset versions and integrate with Git. Follow the steps below to install and configure DVC, set up local remote storage, and manage your datasets.

## Tasks

### 1. Install DVC

- **Command:** `pip install dvc`
- **Objective:** Install the DVC package using pip.

### 2. Initialize DVC

- **Command:** `dvc init`
- **Objective:** Initialize DVC in your project directory to start tracking data files.

### 3. Set Up Local Remote Storage

#### Create a Storage Directory

- **Command:** `mkdir /path/to/your/local/storage`
- **Objective:** Create a local directory to store your versioned data.

#### Add the Storage as a DVC Remote

- **Command:** `dvc remote add -d localstorage /path/to/your/local/storage`
- **Objective:** Configure DVC to use the local storage directory as the default remote storage.

### 4. Add Your Data

#### Place Your Datasets

- **Objective:** Move your datasets into the project directory.

#### Track Your Data with DVC

- **Command:** `dvc add <data.csv>`
- **Objective:** Use DVC to track changes to your data files.

### 5. Commit Changes to Version Control

- **Objective:** Create different versions of the data by committing `.dvc` files to your Git repository.

#### Commit the .dvc Files

- **Command:** `git add . && git commit -m "Add data version control with DVC"`
- **Objective:** Add and commit the DVC tracking files to Git.

### 6. Push Data to Local Remote

- **Command:** `dvc push`
- **Objective:** Push the data to the configured local remote storage.

## Minimum Essential To-Do

1. **Merge Branches:** Merge the necessary branches from task-1 into the main branch using a Pull Request (PR).
2. **Create a New Branch:** Create a new branch called `task-2`.
   - **Command:** `git checkout -b task-2`
3. **Commit Work:** Commit your changes with a descriptive commit message.
   - **Command:** `git add . && git commit -m "Setup DVC and local storage"`
4. **Install DVC:** Ensure DVC is installed.
5. **Configure Local Remote Storage:** Set up local remote storage as described.
6. **Add Your Data:** Track your datasets with DVC.
7. **Commit Changes:** Commit the `.dvc` files to your Git repository.
8. **Push Data:** Push the data to the local remote storage.

## Notes

- Ensure that your local storage path is correctly specified and accessible.
- Regularly push your data changes to keep your remote storage updated.
- Use descriptive commit messages to keep track of changes effectively.

## Contact

For any questions or further assistance, please contact Mitiku Dinsamo at Mitikudinsamo@gmail.com.


