# Importing pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# Step 1 & 2
print(census.head())

# Step 3
print(census.dtypes)


# Step 4

print(census['birth_year'].unique())


# Step 5

# converting birth_year column from obj dtype to int

"""

ValueError: invalid literal for int() with base 10: 'missing'

"""

# need to fix the missing values in birth_year column before conversion

census['birth_year'] = census['birth_year'].replace('missing', 1967)


# Step 6

census['birth_year'] = census['birth_year'].astype("int")

print(census.dtypes)

# Step 7
# average birth year of respondents

print(census['birth_year'].mean())

 # Step 8

# Converting the higher_tax column to categorical data

census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

# printing out unique values in the higher_tax column

print(census['higher_tax'].unique())


# Step 9

# Creating the higher_tax variable by encoding higher taxes sentiment

census['higher_tax'] = census['higher_tax'].cat.codes
# print(census.head(10))

print(census['higher_tax'].median())


# Step 10

# Use get_dummies to OHE the marital_status
census = pd.get_dummies(census, columns=['marital_status'])

# first 5 rows in the census dataframe
print(census.head())


# Step 11

# Create a new variable called marital_codes by Label Encoding the marital_status variable.

# # Ensure marital_status is a categorical type
# census['marital_status'] = census['marital_status'].astype('category')

# # Create marital_codes by label encoding the marital_status variable
# census['marital_codes'] = census['marital_status'].cat.codes

# # Print the first few rows to verify
# print(census[['marital_status', 'marital_codes']].head())


# Create a new variable called age_group, which groups respondents based on their birth year.

#1 - defining current year

current_year = 2024

census['age'] = current_year - census['birth_year']


import pandas as pd

# Assuming the current year is 2023
current_year = 2023

# Calculate age
census['age'] = current_year - census['birth_year']

# Creating age groups in five-year increments
census['age_group'] = pd.cut(census['age'], bins=range(0, 100, 5), right=False)  # which means it is left side inlcusive i.e 0-4, 5-9,..

"""
[a, b) means:
The interval includes a (left endpoint is inclusive) and excludes b (right endpoint is exclusive).
"""

# Label encode the age_group variable
census['age_group_codes'] = pd.Categorical(census['age_group']).codes

# Print the first few rows to verify
print(census[['birth_year', 'age', 'age_group', 'age_group_codes']].head())



