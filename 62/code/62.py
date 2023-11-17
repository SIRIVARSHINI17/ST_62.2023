import numpy as np

# Define the birth rates and death rates
lambda_values = [1, 1, 2, 0]
mu_values = [0, 1, 1, 1]

# Number of states
n = len(lambda_values)

# Define pi_0 (initial probability distribution)
pi_0 = 1.0  # You can set it to any non-zero value

# Calculate the stationary distribution using the formula
stationary_distribution = np.zeros(n)
stationary_distribution[0] = pi_0

for i in range(1, n):
    stationary_distribution[i] = (lambda_values[i-1] / mu_values[i]) * stationary_distribution[i-1]

# Normalize the stationary distribution to sum to 1
stationary_distribution /= np.sum(stationary_distribution)
y= (stationary_distribution[0]+2*stationary_distribution[1]+ 3*stationary_distribution[2]+ 4*stationary_distribution[3]).round(3)

print(y)

