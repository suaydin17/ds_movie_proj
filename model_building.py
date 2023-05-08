# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:53:52 2023

@author: susum
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Load the data from a CSV file
df = pd.read_csv("C:/Users/susum/Documents/ds_movie_proj/eda_data.csv")

# Select the relevant columns for our model
X = df[['Domestic Sales (in $)', 'International Sales (in $)', 'Total Runtime (min)']]
y = df['World Sales (in $)']

# Create a linear regression model and calculate the cross-validation score
lr = LinearRegression()
cv_scores = cross_val_score(lr, X, y, cv=5)

# Print the mean of the cross-validation scores
print("Cross-validation scores:", cv_scores)
print("Mean cross-validation score:", cv_scores.mean())