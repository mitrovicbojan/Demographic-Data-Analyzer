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
#print(male_avg_age)

#What is the percentage of people who have a Bachelor's degree?

edu_counts = X['education'].value_counts().reset_index()

edu_counts.columns = ['education', 'count']

bs_deg_holder = edu_counts[edu_counts['education'] == 'Bachelors']['count'].sum()

bs_deg_perc = (bs_deg_holder / edu_counts['count'].sum()) * 100 

#print("Percentage of people who have a Bachelor's degree is:", bs_deg_perc.round(2),"%")

#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

df = pd.concat([X, y], axis=1)

# clean dot in income column
df['income'] = df['income'].str.replace('.', '', regex=False).str.strip()
bs_nums = df[['education', 'income']].value_counts().reset_index(name='count')

#(cond1) & (cond2) — both conditions must be in parentheses, 
#otherwise Python tries to apply & between mismatched types (like Series and strings)

ttl_num_bachelors = bs_nums[bs_nums['education'] == 'Bachelors']['count'].sum()
high_income_bachelors = bs_nums[(bs_nums['education'] == 'Bachelors') & (bs_nums['income'] == '>50K')]['count'].sum()

bs_with_higher_income = (high_income_bachelors / ttl_num_bachelors) * 100

#print(bs_with_higher_income.round(2))

high_edu_nums = bs_nums[
    bs_nums['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
]['count'].sum()

high_edu_high_income = bs_nums[
    bs_nums['education'].isin(['Bachelors', 'Masters', 'Doctorate']) &
    (bs_nums['income'] == '>50K')
]['count'].sum()

res_high_income_edu = (high_edu_high_income / high_edu_nums) * 100

print(res_high_income_edu.round(2))

#What percentage of people without advanced education make more than 50K?
#note: write a function for this one