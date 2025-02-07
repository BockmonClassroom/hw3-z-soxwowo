# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import os

# Define file paths
file_t1 = "../Data/t1_user_active_min.csv"
file_t2 = "../Data/t2_user_variant.csv"
output_file = "../part4/t1_t2_cleaned_data.csv"

# Check if files exist before proceeding
if not os.path.exists(file_t1) or not os.path.exists(file_t2):
    raise FileNotFoundError("One or both input files are missing. Please check the 'Data' directory.")

# Load the datasets
t1 = pd.read_csv(file_t1)
t2 = pd.read_csv(file_t2)

# Process Table 1 (User Activity Data), Remove duplicate rows
t1 = t1.drop_duplicates()

# Define an upper limit for active minutes (12 hours = 720 minutes)
t1 = t1[t1["active_mins"] <= 720]

# Drop the date column as we only need aggregated total playtime
t1 = t1.drop(columns=['dt'])

# Aggregate total playing time per user
t1 = t1.groupby("uid")["active_mins"].sum().reset_index()

# Rename column for clarity
t1.rename(columns={"active_mins": "total_act_mins"}, inplace=True)

# Process Table 2 (Experiment Group Data), Remove duplicate rows
t2 = t2.drop_duplicates()

# Merge cleaned user activity data with experiment group information
data = pd.merge(t1, t2[["uid", "variant_number"]], on="uid", how="left")

# Save cleaned dataset
data.to_csv(output_file, index=False)

print(f"Outliers removed and cleaned data saved to {output_file}")
print(data.head())
