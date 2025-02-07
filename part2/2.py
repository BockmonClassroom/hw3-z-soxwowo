# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import os

# Define file paths for input datasets
input_dir = "../Data"
file_t1 = os.path.join(input_dir, "t1_user_active_min.csv") 
file_t2 = os.path.join(input_dir, "t2_user_variant.csv")
output_file = "organized_user_data.csv"  # Store in the same directory as the script

# Read the datasets into Pandas DataFrames
t1 = pd.read_csv(file_t1)
t2 = pd.read_csv(file_t2)

# Process t1 (user activity data), Remove duplicate rows to ensure data integrity
t1 = t1.drop_duplicates()

# Aggregate total active minutes per user by summing across all recorded days
t1 = t1.groupby("uid")["active_mins"].sum().reset_index()

# Rename the column to indicate total active minutes recorded after the experiment started
t1.rename(columns={"active_mins": "total_act_mins"}, inplace=True)

# Process t2 (experiment group data), Remove duplicate rows to ensure each user is uniquely assigned to a variant group
t2 = t2.drop_duplicates()

# Merge user activity data with experiment group assignments
# This step links each user’s total activity minutes with their experiment variant
data = pd.merge(t1, t2[["uid", "variant_number"]], on="uid", how="left")

# Save the processed dataset to a CSV file in the same directory
data.to_csv(output_file, index=False)

# Print confirmation message after successful processing
print(f"Organized data has been saved to {output_file}")
