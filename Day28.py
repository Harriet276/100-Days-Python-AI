#Day 28 – GroupBy, Aggregation, and Sorting in Pandas
import pandas as pd

# Q1:
#
# Create a DataFrame with:
#
# Name	 Subject	 Score
# Alice  Math	    80
# Bob 	 Science 	75
# Alice  Science    85
# Bob	 Math	   70
#
# Group the data by student name and find their average score.

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
    'Subject':['Math', 'Science', 'Math', 'Science'],
    'Score': [80, 75,85,70]
})
print(df.groupby('Name')['Score'].mean())


# Q2:
# Using the same DataFrame, group by subject and return:
# Average score
# Number of students per subject

print(df.groupby('Subject')['Score'].mean())
print(df.groupby('Subject')['Score'].count())

# Q3:
# Sort the grouped subject average scores in descending order.
print('      ')
print(df.groupby('Subject')['Score'].mean().sort_values(ascending=False))

# print(df.groupby('Subject')['Score'].sort(ascending=False))