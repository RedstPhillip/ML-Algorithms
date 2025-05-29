# 🌟 Machine Learning Project

Welcome to the **Machine Learning Project**! This project is a collection of machine learning algorithms implemented in Python from scratch. Currently, it includes linear regression and logistic regression models, and it is designed to be expanded with more algorithms in the future.

## 📚 Table of Contents
- [🌟 Introduction](#\🌟-introduction)
- [📈 Linear Regression](#\📈-linear-regression)
  - [📊 Generating the Training Set](#\📊-generating-the-training-set)
  - [🧠 Training the Model](#\🧠-training-the-model)
- [🚦 Logistic Regression](#\🚦-logistic-regression)
  - [📊 Generating the Training Set](#\📊-generating-the-training-set-1)
  - [🧠 Training the Model](#\🧠-training-the-model-1)
- [🚀 Future Work](#\🚀-future-work)

## 🌟 Introduction
This project provides implementations of various machine learning algorithms from scratch. It serves as an educational tool and as a foundation for more complex projects.

## 📈 Linear Regression
Linear regression is a simple yet powerful algorithm for predicting a continuous target variable based on one or more input features. The goal is to find the best-fitting straight line through the data points that minimizes the sum of the squared differences between the observed values and the values predicted by the line.

### 📊 Generating the Training Set
The training set for the linear regression model is generated using the `linear-regression/generate_training_set.py` script. This script creates a dataset with a specified number of features, weights, bias, and noise level.

### 🧠 Training the Model
The project includes implementations for both single and multiple feature linear regression:
- **Single Feature**: `LR_1Feature.ipynb`
- **Multiple Features**: `LR_MultipleFeature.ipynb`

Both notebooks utilize gradient descent with features such as z-score normalization and early convergence detection.

## 🚦 Logistic Regression
Logistic regression is used for binary classification. It estimates probabilities using the logistic function, and the decision boundary is computed based on these probabilities.

### 📊 Generating the Training Set
The logistic regression training set is generated using the `logistic-regression/generate_training_set.py` script. This script creates random features and binary labels for testing the logistic regression code.

### 🧠 Training the Model
The logistic regression model is implemented in the `logistic-regression/LG_MultiFeature.ipynb` notebook. The notebook includes:
- Reading and normalizing the training data
- Computing predictions using the logistic function
- Optimizing parameters via gradient descent
- Printing and plotting the decision boundary (for 2 features)

## 🚀 Future Work
The project is designed to be expanded with additional machine learning algorithms. Some potential additions include:
- Polynomial Regression
- Neural Networks
- Decision Trees
- Random Forests
- Boosted Trees
- Unsupervised Learning
- Reinforcement Learning