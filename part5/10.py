# DS5110
# HW3
# Jitong Zou
# Feb 7, 2025

import pandas as pd
import scipy.stats as stats
import pingouin as pg
import numpy as np
import researchpy as rp
from statsmodels.stats.weightstats import ttest_ind
import os

# Define file path for the new dataset
file_path = "t1_t2_t3.csv"

# Check if file exists before proceeding
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File {file_path} not found. Please ensure the file exists in the 'part5' directory.")

# Load the merged dataset
df = pd.read_csv(file_path)

# Apply a stricter threshold (12-hour threshold = 720 minutes) to remove extreme values
df = df[(df["total_act_mins_post"] <= 720) & (df["total_act_mins_pre"] <= 720)]

# Split the two groups based on variant_number
group1_post = df[df["variant_number"] == 0]["total_act_mins_post"]
group1_pre = df[df["variant_number"] == 0]["total_act_mins_pre"]
group2_post = df[df["variant_number"] == 1]["total_act_mins_post"]
group2_pre = df[df["variant_number"] == 1]["total_act_mins_pre"]

# Perform the two sample t-test with five different methods
# Method 1: Using Scipy library for t-test
res1_control = stats.ttest_ind(a=group1_post, b=group1_pre, equal_var=True)
res1_treatment = stats.ttest_ind(a=group2_post, b=group2_pre, equal_var=True)

# Method 2: Two-Sample T-Test with Pingouin
res2_control = pg.ttest(group1_post, group1_pre, correction=True)
res2_treatment = pg.ttest(group2_post, group2_pre, correction=True)

# Method 3: Two-Sample T-Test with Statsmodels
res3_control = ttest_ind(group1_post, group1_pre)
res3_treatment = ttest_ind(group2_post, group2_pre)

# Method 4: Compute t-statistic manually using numpy
mean1_post, mean1_pre = np.mean(group1_post), np.mean(group1_pre)
std1_post, std1_pre = np.std(group1_post, ddof=1), np.std(group1_pre, ddof=1)
n1_post, n1_pre = len(group1_post), len(group1_pre)
t_stat_manual_control = (mean1_post - mean1_pre) / np.sqrt((std1_post**2 / n1_post) + (std1_pre**2 / n1_pre))

mean2_post, mean2_pre = np.mean(group2_post), np.mean(group2_pre)
std2_post, std2_pre = np.std(group2_post, ddof=1), np.std(group2_pre, ddof=1)
n2_post, n2_pre = len(group2_post), len(group2_pre)
t_stat_manual_treatment = (mean2_post - mean2_pre) / np.sqrt((std2_post**2 / n2_post) + (std2_pre**2 / n2_pre))

# Method 5: Two-Sample T-Test with ResearchPy
summary_control, res5_control = rp.ttest(group1_post, group1_pre)
summary_treatment, res5_treatment = rp.ttest(group2_post, group2_pre)

# Compute mean and median for each group
control_post_mean, control_post_median = group1_post.mean(), group1_post.median()
control_pre_mean, control_pre_median = group1_pre.mean(), group1_pre.median()
treatment_post_mean, treatment_post_median = group2_post.mean(), group2_post.median()
treatment_pre_mean, treatment_pre_median = group2_pre.mean(), group2_pre.median()

# Print results
print("Statistical Analysis Results:")
print("========================================")
print("Control Group - Scipy T-Test Result:", res1_control)
print("========================================")
print("Control Group - Pingouin T-Test Result:\n", res2_control)
print("========================================")
print("Control Group - Statsmodels T-Test Result:", res3_control)
print("========================================")
print(f"Control Group - Manual T-Test (NumPy): t-statistic = {t_stat_manual_control:.4f}")
print("========================================")
print("Control Group - ResearchPy T-Test Result:\n", res5_control)
print("========================================")
print(f"Control Group - Mean Pre: {control_pre_mean:.2f}, Post: {control_post_mean:.2f}")
print(f"Control Group - Median Pre: {control_pre_median:.2f}, Post: {control_post_median:.2f}")

print("========================================")
print("Treatment Group - Scipy T-Test Result:", res1_treatment)
print("========================================")
print("Treatment Group - Pingouin T-Test Result:\n", res2_treatment)
print("========================================")
print("Treatment Group - Statsmodels T-Test Result:", res3_treatment)
print("========================================")
print(f"Treatment Group - Manual T-Test (NumPy): t-statistic = {t_stat_manual_treatment:.4f}")
print("========================================")
print("Treatment Group - ResearchPy T-Test Result:\n", res5_treatment)
print("========================================")
print(f"Treatment Group - Mean Pre: {treatment_pre_mean:.2f}, Post: {treatment_post_mean:.2f}")
print(f"Treatment Group - Median Pre: {treatment_pre_median:.2f}, Post: {treatment_post_median:.2f}")
