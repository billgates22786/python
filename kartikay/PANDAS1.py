import pandas as pd

# Data to be stored in the Pandas Series
data1 = [10, 20, 40, 80, 100]
data2 = [150, 200]

# Create two Series using the Series() method
series1 = pd.Series(data1, index=["RowA", "RowB", "RowC", "RowD", "RowE"])
series2 = pd.Series(data2, index=["RowF", "RowG"])

# Display the Series
print("Series1 (with custom index labels): \n", series1)
print("\nSeries2 (with custom index labels): \n", series2)

# Append
result = series1.append(series2, ignore_index=False)

# Print the result
print("\nResult after appending (considering original indexes):\n", result)
