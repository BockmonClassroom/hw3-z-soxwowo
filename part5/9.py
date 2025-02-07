# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import os

# Define file paths
file_t1_t2_cleaned = "../part4/t1_t2_cleaned_data.csv"
file_t3 = "../Data/t3_user_active_min_pre.csv"
output_file = "../part5/t1_t2_t3.csv"

# Check if files exist before proceeding
if not os.path.exists(file_t1_t2_cleaned) or not os.path.exists(file_t3):
    raise FileNotFoundError("One or both input files are missing. Please check the 'Data' directory.")

# Load the datasets
t1_t2_cleaned = pd.read_csv(file_t1_t2_cleaned)
t3 = pd.read_csv(file_t3)

# Rename post-experiment total minutes for clarity
t1_t2_cleaned.rename(columns={"total_act_mins": "total_act_mins_post"}, inplace=True)

# Process Table 3 (Pre-Experiment User Activity Data), Remove duplicate rows
t3 = t3.drop_duplicates()

# Define an upper limit for active minutes (12 hours = 720 minutes)
t3 = t3[t3["active_mins"] <= 720]

# Drop the date column as we only need aggregated total playtime
t3 = t3.drop(columns=['dt'])

# Aggregate total playing time per user
t3 = t3.groupby("uid")["active_mins"].sum().reset_index()

# Rename column for clarity
t3.rename(columns={"active_mins": "total_act_mins_pre"}, inplace=True)

# Merge cleaned user activity data with experiment group information
data = pd.merge(t1_t2_cleaned, t3[["uid", "total_act_mins_pre"]], on="uid", how="left")

# Fill missing pre-experiment values with 0 (assuming no prior activity)
data["total_act_mins_pre"].fillna(0, inplace=True)

# Save cleaned dataset
data.to_csv(output_file, index=False)

# Print output details
print(f"Outliers removed and cleaned data saved to {output_file}")
print(f"Number of users in cleaned dataset (post-experiment): {len(t1_t2_cleaned)}")
print(f"Number of users in pre-experiment data (t3): {len(t3)}")
print(f"Final merged dataset size: {len(data)}")
print(data.head())
