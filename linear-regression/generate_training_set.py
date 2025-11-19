import numpy as np
import pandas as pd

# Parameters for the dataset
num_features = 10         # Number of input features
num_points = 100000        # Number of data points
feature_range = (-1000, 1000)  # Range for feature values (min, max)
weights = np.random.uniform(100, 100, num_features)  # Random weights (slopes)
bias = -2000.0           # Intercept
noise_factor = 1000.0     # Noise level

# Generate the dataset
np.random.seed(42)  # For reproducibility
features = np.random.uniform(feature_range[0], feature_range[1], (num_points, num_features))  # Random features
noise = np.random.normal(0, noise_factor, num_points)  # Add noise
y = np.dot(features, weights) + bias + noise  # Compute target variable

# Save the dataset to a CSV file
data = {f'x{i+1}': features[:, i] for i in range(features.shape[1])}
data['y'] = y
df = pd.DataFrame(data)
csv_file = "training_data.csv"
df.to_csv(csv_file, index=False)

print(f"Dataset saved to {csv_file}")
