# 0105-ADV-ML-II-Dimensionality-reduction-weekly-project

## Overview
This project aims to explore and apply feature Engineering and dimensionality reduction techniques on second-hand car sales datasets. The goal is to prepare the dataset for machine learning models by creating informative features and reducing the feature space while retaining essential information. 

## Project Steps:
1. Introduction
2. Dataset Overview
3. Data Preparation
4. Feature Engineering
5. Dimensionality reduction
6. Modelling and Evaluation
7. Conclusion


## 1. Introduction
The second-hand car market is vast, and predicting the price of a used car is a challenging task due to various factors influencing the price. Feature engineering and dimensionality reduction play a crucial role in improving the performance of predictive models by enhancing the quality of input data and reducing noise.

## 2. Dataset Overview
We will use a second-hand car sales dataset containing features such as make, model, year, mileage, state, price, etc. The dataset can be obtained from public repositories like Kaggle or scraped from online car listing websites.

## 3. Data Preprocessing
### 3.1. Loading the Data
### 3.2. Data Cleaning
Handling Missing Values: Identify and handle missing values by either removing or imputing them.
Removing Duplicates: Check and remove duplicate rows.
Data Type Conversion: Ensure all features have appropriate data types.

## 4. Feature Engineering
### 4.1. Creating New Features
Car Age: Calculate the age of the car from the year of manufacture.
Price per Mile: Compute price per mile as a new feature.

### 4.2. Encoding Categorical Features
One-Hot Encoding: Apply one-hot encoding to categorical features like make, model, state, color, transmission, and fuel.

### 4.3. Feature Scaling
Standardization: Standardize numerical features to have zero mean and unit variance.

## 5. Dimensionality Reduction
### 5.1. Correlation Analysis
Correlation Matrix: Compute the correlation matrix and remove highly correlated features.

### 5.2. Principal Component Analysis (PCA)
PCA Implementation: Apply PCA to reduce the feature space while retaining most of the variance.

## 6. Modeling and Evaluation
### 6.1. Train-Test Split
Split the data into training and testing sets.
### 6.2. Model Selection
Train multiple models and select the best performing one.

## 7. Conclusion
### 7.1. Summary
Summarize the key findings and improvements from feature engineering and dimensionality reduction.
Highlight the performance of the best model.
### 7.2. Future Work
Suggest additional feature engineering techniques or data sources.
Propose further dimensionality reduction methods or advanced modeling techniques.
