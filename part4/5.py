# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define file path
file_path = "../part2/organized_user_data.csv"

# Check if file exists before proceeding
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File {file_path} not found. Please ensure the file exists in the 'part2' directory.")

# Load the organized dataset
df = pd.read_csv(file_path)

# Create a box plot for Group 1 (Control) and Group 2 (Treatment)
plt.figure(figsize=(8, 6))
sns.boxplot(x=df["variant_number"], y=df["total_act_mins"], palette=["green", "red"])

# Customize plot
plt.xticks([0, 1], ["Control Group", "Treatment Group"], fontsize=12)
plt.xlabel("Group", fontsize=14)
plt.ylabel("Total Active Minutes", fontsize=14)
plt.title("Box Plot of Total Active Minutes for Control and Treatment Groups", fontsize=14)

# Show plot
plt.show()
