#Day 27 – Data Cleaning: Missing Values & Data Types
import numpy as np
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# Q1: Detect and Count Missing Values
# Given a DataFrame with missing entries:
# Show how many missing values are in each column
# Which rows have missing Name?

df= pd.DataFrame({
    'Name': ['Alice', None,'Charlie', ' Hellen', 'Brooke'],
    'Age': [10,15,25,34,None],
    'Grade':['A','A','A','A','A']
})
#
# print(df.isnull().sum())

# Q2: Clean and Fill

# df = pd.DataFrame({
#     'Student': ['A', 'B', 'C', 'D'],
#     'Score': ['80', '75', np.nan, '90']
# })
# Convert 'Score' to numeric
# Fill missing scores with the average
# Convert 'Student' to category type

# df['Score'] =pd.to_numeric(df['Score'])
# df['Score'] = df['Score'].fillna(df['Score'].mean())
# df['Student'] = df['Student'].astype('category')
# print(df)


# Q3: Drop vs Fill
# Load a DataFrame with at least 2 missing values.
# Drop all rows with missing data
# Then reload and fill all missing values with 'Missing' or column average
df.dropna()
print(df)
print('                          ')
df= pd.DataFrame({
    'Name': ['Alice', None,'Charlie', ' Hellen', 'Brooke'],
    'Age': [10,15,25,34,None],
    'Grade':['A','A','A','A','A']
})
df_filled = df.fillna('Missing')
print(df_filled)
print('             ')
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)
