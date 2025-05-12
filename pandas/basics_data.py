import pandas as pd

data_frame = pd.DataFrame({
  "Name": [
    "Braund, Mr. Owen Harris",
    "Allen, Mr. William Henry",
    "Bonnell, Miss. Elizabeth",
  ],
  "Age": [22, 35, 58],
  "Sex": ["male", "male", "female"],
})

print(data_frame)


# Each column in a DataFrame is a Series
# Get the "Age" column
print(data_frame["Age"])


# Series creation
ages = pd.Series([21, 35, 58], name="Age")
print(ages)


# max and min methods
print("Max age:", data_frame["Age"].max())
print("Min age:", data_frame["Age"].min())


# Basic statistics with describe method
print(data_frame.describe())
