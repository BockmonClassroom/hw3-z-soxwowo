# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

# Define file path
file_path = "../part2/organized_user_data.csv"

# Check if file exists before proceeding
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File {file_path} not found. Please ensure the file exists in the 'part2' directory.")

# Load the organized dataset
df = pd.read_csv(file_path)

# Split the two groups
group1 = df[df["variant_number"] == 0]["total_act_mins"]
group2 = df[df["variant_number"] == 1]["total_act_mins"]
total = np.concatenate([group1, group2])

# Print extreme values to check for outliers
print(f"Max Total Active Minutes - Control Group: {group1.max()}")
print(f"Max Total Active Minutes - Treatment Group: {group2.max()}")

# Create separate histograms for Total, Group 1, and Group 2
fig, axes = plt.subplots(3, 1, figsize=(10, 15))  # 3 rows, 1 column layout

# Histogram for Total group
sns.histplot(total, bins=30, color="purple", alpha=0.7, label="Total", ax=axes[0])
axes[0].set_title("Histogram of Total Active Minutes", fontsize=14)
axes[0].set_xlabel("Total Active Minutes", fontsize=12)
axes[0].set_ylabel("Count", fontsize=12)
axes[0].legend()

# Histogram for Group 1 (Control)
sns.histplot(group1, bins=30, color="green", alpha=0.7, label="Group 1 (Control)", ax=axes[1])
axes[1].set_title("Histogram of Control Group (Group 1)", fontsize=14)
axes[1].set_xlabel("Total Active Minutes", fontsize=12)
axes[1].set_ylabel("Count", fontsize=12)
axes[1].legend()

# Histogram for Group 2 (Treatment)
sns.histplot(group2, bins=30, color="red", alpha=0.7, label="Group 2 (Treatment)", ax=axes[2])
axes[2].set_title("Histogram of Treatment Group (Group 2)", fontsize=14)
axes[2].set_xlabel("Total Active Minutes", fontsize=12)
axes[2].set_ylabel("Count", fontsize=12)
axes[2].legend()

# Adjust layout for better spacing
plt.tight_layout()
plt.show()

# ==========================
# Add Q-Q Plots for Normality Check
# ==========================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Q-Q Plot for Control Group
stats.probplot(group1, dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot: Control Group")

# Q-Q Plot for Treatment Group
stats.probplot(group2, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot: Treatment Group")

# Q-Q Plot for Total Data
stats.probplot(total, dist="norm", plot=axes[2])
axes[2].set_title("Q-Q Plot: Total Data")

plt.tight_layout()
plt.show()
