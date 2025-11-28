# Day 26 – Data Loading (CSV, Excel), Indexing & Selection in Pandas
import pandas as pd

# Q1: Load CSV Data
# Download or use any small CSV file (e.g., from Kaggle or a dataset you've worked on).
# Load the file using pd.read_csv()
# Print the shape, columns, and first 5 rows
# Set a column like 'Name' or 'ID' as the index

# df = pd.read_csv('AI_Tools_List.csv',encoding='latin1')
# print(df.head(9))
# print(df[ (df.Estimated_Valuation_Billion_USD >1)].head(3))
# print("       n\"")
# print(df.iloc[4], df.loc[2])
# print(df.loc[2])
# print("    emptyyyy   n\"")
# print(df[['AI Name', 'AI Type']])

# Q2: Load Excel File
# Download a .xlsx file or create one using Excel/Google Sheets.
# Load the Excel file
# Print the first 3 rows and column names
# Read only a specific sheet using sheet_name=

df= pd.read_excel('Dummydata01.xlsx')
print(df.head(3))
print(df[ ['Age']])
print(df[['Name', 'Age']])
print(df.columns)
print(df.loc[1])



# Q3: Filter and Slice
# Using a loaded DataFrame:
# Extract all rows where 'Age' > 20
# Get the first 3 rows and only columns 'Name' and 'Age'
# Print the row at position 4 and label 2 (if they’re different)
print("           ")
print(df[df['Age'] > 20])
print("       ")
print( df[['Name', 'Age']].iloc[:3])
