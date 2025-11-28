# ------------------------------------------------------------
# TASK 2: Exploratory Data Analysis (EDA)
# Dataset: Tips Dataset (Seaborn Built-in)
# Author: Muhammad Saeed
# Description:
#   This script performs basic EDA on the Tips dataset including:
#   - Data inspection
#   - Summary statistics
#   - Missing value analysis
#   - Visualizations (histogram, scatter plot, count plot)
# ------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------
df = sns.load_dataset("tips")
print("First 5 Rows of Dataset:")
print(df.head())

# ------------------------------------------------------------
# Dataset Info
# ------------------------------------------------------------
print("\nDataset Info:")
print(df.info())

# ------------------------------------------------------------
# Summary Statistics
# ------------------------------------------------------------
print("\nSummary Statistics:")
print(df.describe())

# ------------------------------------------------------------
# Missing Values
# ------------------------------------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------------------------
# Unique Values in Categorical Column
# ------------------------------------------------------------
print("\nUnique values in 'day' column:")
print(df['day'].unique())

# ------------------------------------------------------------
# Visualization 1: Distribution of Total Bill
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
plt.hist(df['total_bill'])
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Visualization 2: Total Bill vs Tip (Scatter Plot)
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
plt.scatter(df['total_bill'], df['tip'])
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Visualization 3: Customer Count Per Day
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x='day', data=df)
plt.title("Customers per Day")
plt.xlabel("Day")
plt.ylabel("Count")
plt.tight_layout()
plt.show()