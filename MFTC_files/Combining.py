# -*- coding: utf-8 -*-
"""
Created on Wed May 24 22:28:30 2023

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt

#parameters
alpha = 2  #pareto dist shape param
size = 1000  #size of simulated data
k = 50  #number of top order statistics to use for the Hill estimator
gamma_true = 0.5  #true value of gamma for frechet domain of attraction
n_repeat = 500  #umber of repetitions

#simulate data from Pareto distribution
def simulate_pareto(alpha, size):
    return np.random.pareto(alpha, size) + 1

#estimate γ using Hill estimator
def hill_estimator(data, k):
    sorted_data = np.sort(data)
    top_k_values = sorted_data[-k:]
    return 1 / np.mean(np.log(top_k_values / sorted_data[-k-1]))

#Repeat for 500 times
errors = []
for _ in range(n_repeat):
    simulated_data = simulate_pareto(alpha, size)
    gamma_hat = hill_estimator(simulated_data, k)
    error = gamma_hat - gamma_true
    errors.append(error)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.boxplot(errors)
plt.title("Boxplot of Errors")
plt.subplot(1, 2, 2)
plt.hist(errors, bins=20, density=True, edgecolor='black')
plt.title("Histogram of Errors")
plt.tight_layout()
plt.show()
errors = np.array(errors)
q1 = np.percentile(errors, 25)
q3 = np.percentile(errors, 75)
iqr = q3 - q1
median = np.median(errors)
lower_whisker = q1 - 1.5 * iqr
upper_whisker = q3 + 1.5 * iqr
outliers = errors[(errors < lower_whisker) | (errors > upper_whisker)]
print(f"Q1: {q1}")
print(f"Median: {median}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Lower Whisker: {lower_whisker}")
print(f"Upper Whisker: {upper_whisker}")
print(f"Outliers: {outliers}")
