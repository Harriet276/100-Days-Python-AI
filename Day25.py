#Day 25 – Pandas Basics: Series & DataFrames
from operator import index
from turtle import pd
import pandas as pd


# Q1: Create a Student Info DataFrame
# Create a DataFrame with columns:
# Name → 5 student names
# Age → their ages
# Grade → A, B, C...
# Then:
# Print first 3 rows using df.head()
# Show the shape of the DataFrame


Data = {
    'Name': [ 'Bob', 'Jim', 'Hannah', 'Hellen', 'Bertha'],
    'Age' : [10,5,15,7,20],
    'Grade': ['A','B','A','A','A']
}

df= pd.DataFrame(Data)
print(df.head(3))

# Q2: Series Indexing
# Create a Series of 5 country populations:
# Use country names as index
# Get population of Tanzania
# Change population of Kenya

Population= pd.Series([100000000, 20000000,3000000,400000,2100000], index = ["Tanzania", "Kenya","Portugal", "Amsterdam","United States"])
Tanzania_population = Population["Tanzania"]
print(Tanzania_population)