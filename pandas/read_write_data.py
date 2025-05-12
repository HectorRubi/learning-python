import pandas as pd

# Read CSV file
titanic = pd.read_csv("data/titanic.csv")

# Display the first and last 5 rows
print(titanic)

# Display the first 8 rows
print(titanic.head(8))

# Display the last 10 rows
print(titanic.tail(10))

# Display the data types of each column
print(titanic.dtypes)

# Convert data to a Excel file
titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

# Read the Excel file
titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")
print(titanic.head())

# Display technical summary of the DataFrame
print(titanic.info())
