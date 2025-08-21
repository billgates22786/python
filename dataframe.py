import pandas as pd

# 1. Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2. Accessing columns
print("\n'Name' column:")
print(df['Name'])

# 3. Adding a new column
df['Salary'] = [50000, 60000, 55000, 70000]
print("\nDataFrame after adding 'Salary' column:")
print(df)

# 4. Filtering rows based on a condition
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# 5. Dropping a column
df = df.drop('City', axis=1) # axis=1 indicates column
print("\nDataFrame after dropping 'City' column:")
print(df)

# 6. Adding a new row
new_row = {'Name': 'Eve', 'Age': 28, 'Salary': 52000}
df.loc[len(df)] = new_row
print("\nDataFrame after adding a new row:")
print(df)

# 7. Basic descriptive statistics
print("\nDescriptive statistics for 'Salary':")
print(df['Salary'].describe())