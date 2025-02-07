# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define file paths
file_t1_t2_t3 = "../part5/t1_t2_t3.csv"
file_t4 = "../Data/t4_user_attributes.csv"
output_file = "../part6/t1_t2_t3_t4.csv"

# Check if files exist before proceeding
if not os.path.exists(file_t1_t2_t3) or not os.path.exists(file_t4):
    raise FileNotFoundError("One or both input files are missing. Please check the 'Data' directory.")

# Load datasets
t1_t2_t3 = pd.read_csv(file_t1_t2_t3).drop_duplicates()
t4 = pd.read_csv(file_t4).drop_duplicates()

# Merge datasets on uid
data = pd.merge(t1_t2_t3, t4, on="uid", how="left")

# Save merged dataset for further analysis
data.to_csv(output_file, index=False)

# Statistical Analysis by User Type
user_types = data["user_type"].unique()
print("\nUser Type Analysis:\n")
for user_type in user_types:
    group = data[data["user_type"] == user_type]
    pre_mean = group["total_act_mins_pre"].mean()
    post_mean = group["total_act_mins_post"].mean()
    t_stat, p_val = stats.ttest_ind(group["total_act_mins_post"], group["total_act_mins_pre"], equal_var=True)
    print(f"{user_type}: Pre-Mean = {pre_mean:.2f}, Post-Mean = {post_mean:.2f}, T-Stat = {t_stat:.4f}, P-Value = {p_val:.4f}")

# Statistical Analysis by Gender
genders = data["gender"].unique()
print("\nGender Analysis:\n")
for gender in genders:
    group = data[data["gender"] == gender]
    pre_mean = group["total_act_mins_pre"].mean()
    post_mean = group["total_act_mins_post"].mean()
    t_stat, p_val = stats.ttest_ind(group["total_act_mins_post"], group["total_act_mins_pre"], equal_var=True)
    print(f"{gender}: Pre-Mean = {pre_mean:.2f}, Post-Mean = {post_mean:.2f}, T-Stat = {t_stat:.4f}, P-Value = {p_val:.4f}")

# Visualization: Boxplot for User Type
plt.figure(figsize=(10, 6))
sns.boxplot(x="user_type", y="total_act_mins_post", data=data)
plt.title("Post-Experiment Activity by User Type")
plt.xlabel("User Type")
plt.ylabel("Total Active Minutes (Post)")
plt.xticks(rotation=45)
plt.show()

# Visualization: Boxplot for Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x="gender", y="total_act_mins_post", data=data)
plt.title("Post-Experiment Activity by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Active Minutes (Post)")
plt.show()

print("Analysis and visualization complete. Insights can be derived from the boxplots and statistical results.")
