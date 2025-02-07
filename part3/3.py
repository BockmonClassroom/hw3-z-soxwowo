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

# Perform the two sample t-test with five different methods
# Method 1: Using Scipy library for t-test
res1 = stats.ttest_ind(a=group1, b=group2, equal_var=True)

# Method 2: Two-Sample T-Test with Pingouin
res2 = pg.ttest(group1, group2, correction=True)

# Method 3: Two-Sample T-Test with Statsmodels
res3 = ttest_ind(group1, group2)

# Method 4: Compute t-statistic manually using numpy
mean1, mean2 = np.mean(group1), np.mean(group2)
std1, std2 = np.std(group1, ddof=1), np.std(group2, ddof=1)
n1, n2 = len(group1), len(group2)
t_stat_manual = (mean1 - mean2) / np.sqrt((std1**2 / n1) + (std2**2 / n2))

# Method 5: Two-Sample T-Test with ResearchPy
summary, res5 = rp.ttest(group1, group2)

# Compute mean and median for each group
control_mean, control_median = group1.mean(), group1.median()
treatment_mean, treatment_median = group2.mean(), group2.median()

# Print results
print("Statistical Analysis Results:")
print("========================================")
print("Scipy T-Test Result:", res1)
print("========================================")
print("Pingouin T-Test Result:\n", res2)
print("========================================")
print("Statsmodels T-Test Result:", res3)
print("========================================")
print(f"Manual T-Test Result (NumPy): t-statistic = {t_stat_manual:.4f}")
print("========================================")
print("ResearchPy T-Test Result:\n", res5)
print("========================================")
print(f"Control Group - Mean: {control_mean:.2f}, Median: {control_median:.2f}")
print(f"Treatment Group - Mean: {treatment_mean:.2f}, Median: {treatment_median:.2f}")
