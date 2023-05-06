# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:49:54 2023

@author: susum
"""

import pandas as pd
import numpy as np

df= pd.read_csv('C:/Users/susum/Documents/ds_movie_proj/Highest Holywood Grossing Movies.csv')

#drop unnamed column
df.drop('Unnamed: 0', axis=1, inplace=True)

#omit the year info from movie title
df['Title'] = df['Title'].str.split(r'\s\(\d{4}\)').str[0]

#divide the release date as year and month
df['Year'] = pd.to_datetime(df['Release Date']).dt.year
df['Month'] = pd.to_datetime(df['Release Date']).dt.month_name()

#age of movie
df['Age'] = 2023 - df['Year']

#runtime to minutes
hours = df['Movie Runtime'].str.extract('(\d+) hr', expand=False).fillna(0).astype(int)
minutes = df['Movie Runtime'].str.extract('(\d+) min', expand=False).fillna(0).astype(int)
df['Total Runtime (min)'] = hours * 60 + minutes

df.to_csv('movies_data_cleaned.csv', index=False)