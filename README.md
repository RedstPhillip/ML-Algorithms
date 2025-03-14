# 🌟 Machine Learning Project

Welcome to the **Machine Learning Project**! This project is a collection of machine learning algorithms implemented in Python from scratch. Currently, it includes a linear regression model, but it is designed to be expanded with more algorithms in the future.

## 📚 Table of Contents
- [🌟 Introduction](#-introduction)
- [📈 Linear Regression](#-linear-regression)
  - [📊 Generating the Training Set](#-generating-the-training-set)
  - [🧠 Training the Model](#-training-the-model)
- [🚀 Future Work](#-future-work)

## 🌟 Introduction
This project aims to provide implementations of various machine learning algorithms from scratch. It is intended for educational purposes and to serve as a starting point for more complex projects.

## 📈 Linear Regression
Linear regression is a simple yet powerful algorithm for predicting a continuous target variable based on one or more input features. The goal is to find the best-fitting straight line through the data points that minimizes the sum of the squared differences between the observed values and the values predicted by the line.

### 📊 Generating the Training Set
The training set for the linear regression model is generated using the `generate_training_set.py` script. This script creates a dataset with a specified number of features, weights, bias, and noise level.

### 🧠 Training the Model
The project includes implementations for both single and multiple feature linear regression:

- **Single Feature**: `LR_1Feature.ipynb` handles regression with one input feature.

- **Multiple Features**: `LR_MultipleFeature.ipynb` extends the implementation to handle multiple input features with:
  - z-score feature normalization
  - Vectorized operations with NumPy
  - Early stopping using epsilon-based convergence detection

Both notebooks follow the gradient descent optimization approach to find the optimal parameters. The gradient descent algorithm:
1. Calculates the model predictions using current parameters
2. Computes the cost (mean squared error) to measure prediction quality
3. Computes gradients to determine the direction of parameter updates
4. Updates parameters to minimize the cost function
5. For multiple features, includes early convergence detection to stop when changes fall below epsilon threshold

For detailed code, please refer to:
- `linear-regression/generate_training_set.py`
- `linear-regression/LR_1Feature.ipynb`
- `linear-regression/LR_MultipleFeature.ipynb`

## 🚀 Future Work
This project is designed to be expanded with more machine learning algorithms in the future. Some potential additions include:
- Polynomial Regression
- Logistic Regression
- Neural Networks
- Decision Trees
- Random Forests
- Boosted Trees
- Unsupervised Learning
- Reinforcement Learning