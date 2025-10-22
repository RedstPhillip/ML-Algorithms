# Machine Learning Project

Welcome to the Machine Learning Project! This project is a collection of machine learning algorithms implemented in Python from scratch. Currently, it includes linear regression and logistic regression models, and it is designed to be expanded with more algorithms in the future.

## Table of Contents
- [Introduction](#introduction)
- [Linear Regression](#linear-regression)
- [Logistic Regression](#logistic-regression)
- [Future Work](#future-work)

## Introduction
This project provides implementations of various machine learning algorithms from scratch. It serves as an educational tool and as a foundation for more complex projects.

## Linear Regression
Linear regression is used for predicting a continuous target variable from one or more input features by fitting a line that minimizes the sum of squared errors. The training set can be generated with `linear-regression/generate_training_set.py` (configurable features, weights, bias, noise). Notebooks:
- `linear-regression/LR_1Feature.ipynb` (single feature)
- `linear-regression/LR_MultipleFeature.ipynb` (multiple features)

Both notebooks use gradient descent with z-score normalization and early convergence detection, and include simple visualizations.

## Logistic Regression
Logistic regression is used for binary classification. It estimates probabilities with the logistic (sigmoid) function, and a decision boundary can be derived from the model. The training set can be generated with `logistic-regression/generate_training_set.py`. Main notebook:
- `logistic-regression/LG_MultiFeature.ipynb`

The notebook covers reading and normalizing data, computing predictions, optimizing parameters via gradient descent, and plotting a decision boundary (for 2 features).

## Future Work
The project is designed to be expanded with additional machine learning algorithms. Potential additions include:
- Polynomial Regression
- Decision Trees
- Random Forests
- Boosted Trees
- Unsupervised Learning
- Reinforcement Learning
- Neural Networks
