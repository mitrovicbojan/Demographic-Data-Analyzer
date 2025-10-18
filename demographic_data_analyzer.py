import numpy as np;
import pandas as pd;

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
census_income = fetch_ucirepo(id=20) 
  
# data (as pandas dataframes) 
X = census_income.data.features 
y = census_income.data.targets 
  
# metadata 
#print(census_income.metadata) 
  
# variable information 
#print(census_income.variables) 

#How many people of each race are represented in this dataset? 
#This should be a Pandas series with race names as the index labels.

# Get count of each unique race
race_counts = X['race'].value_counts().reset_index()

# Rename columns for clarity
race_counts.columns = ['race', 'count']

'''
# Add percentage of each race representatives 
# Add percentage column
race_counts['percentage'] = (race_counts['count'] / race_counts['count'].sum()) * 100 

# Optionally round percentages
race_counts['percentage'] = race_counts['percentage'].round(2)

print(race_counts)
'''

#What is the average age of men?
male_rows = X[X['sex'] == 'Male']

male_avg_age = male_rows['age'].mean().round(2)
print(male_avg_age)