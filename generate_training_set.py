import numpy as np
import pandas as pd

# Parameters for the dataset
w = -500.0  # Slope
b = -1800.0  # Intercept
num_points = 500  # Number of data points
noise_factor = 500.0  # Noise level

# Generate the dataset
x = np.linspace(0, 10, num_points)
noise = np.random.normal(0, noise_factor, num_points)
y = w * x + b + noise

# Save the dataset to a CSV file
data = {'x': x, 'y': y}
df = pd.DataFrame(data)
csv_file = "training_data.csv"
df.to_csv(csv_file, index=False)

print(f"Dataset saved to {csv_file}")
