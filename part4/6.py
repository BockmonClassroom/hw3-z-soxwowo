# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import os

# Define file path
file_path = "../Data/t1_user_active_min.csv"

# Check if file exists before proceeding
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File {file_path} not found. Please ensure the file exists in the 'Data' directory.")

# Load the t1 dataset
t1 = pd.read_csv(file_path)

# Get the maximum recorded active minutes
max_t1 = t1["active_mins"].max()
print(f"Highest value in table 1: {max_t1} minutes")

# Define the realistic daily activity limit
daily_limit = 24*60

# Count how many entries exceed the daily limit
num_outliers = t1[t1["active_mins"] >= daily_limit]["uid"].count()
print(f"Number of entries exceeding {daily_limit} minutes per day: {num_outliers}")

# Extract users with unrealistic active minutes
outliers = t1[t1["active_mins"] >= daily_limit]

# Save the outliers for further inspection
outlier_file = "../part4/outliers_analysis.csv"
outliers.to_csv(outlier_file, index=False)
print(f"Outlier data saved to {outlier_file}")

# Display sample outliers
print("Sample outlier records:")
print(outliers.head())
