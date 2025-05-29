import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_training_data(m=1000, n=2, noise_std=0.5, seed=42):
    """
    Generate a training set for binary classification using a logistic model.

    Parameters:
    - m: Number of examples.
    - n: Number of features.
    - noise_std: Standard deviation of the noise.
    - seed: Random seed for reproducibility.

    Returns:
    - df: pandas DataFrame with n features and a binary target column 'y'.
    """
    np.random.seed(seed)
    X = np.random.randn(m, n)
    true_w = np.random.randn(n)
    true_b = 0.5
    logits = np.dot(X, true_w) + true_b + np.random.randn(m) * noise_std
    probs = 1 / (1 + np.exp(-logits))
    y = (probs > 0.5).astype(int)

    feature_columns = [f'x{i + 1}' for i in range(n)]
    df = pd.DataFrame(X, columns=feature_columns)
    df['y'] = y
    return df


if __name__ == '__main__':
    # Generate training data and save to CSV
    df = generate_training_data(m=1000, n=2)
    df.to_csv('training_data.csv', index=False)
    print("Training data saved to 'training_data.csv'.")

    # Plot the data if there are 2 features
    if df.shape[1] - 1 == 2:
        plt.figure(figsize=(8, 6))
        colors = ['red' if label == 0 else 'blue' for label in df['y']]
        plt.scatter(df['x1'], df['x2'], c=colors, alpha=0.6)
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.title('Scatter Plot of Generated Training Data')
        plt.grid(True)
        plt.show()
