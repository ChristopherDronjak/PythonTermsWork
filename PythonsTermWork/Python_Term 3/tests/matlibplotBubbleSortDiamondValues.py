import pandas as pd
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]['Price'] > arr[j + 1]['Price']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe

# Column names you want to read from the CSV file
columns = [0,4]

# Escaping the backslashes
filepath = 'C:/Users/nzbob/OneDrive/Desktop/Python_Term 3/DiamondValues.csv'

dataframe = read_csv(filepath, columns)

print("Original Data:")
print(dataframe)
print("")

plt.subplot(1,2,1)
plt.plot(dataframe)
plt.ylabel("Data Before Sorting Price:")

# Convert DataFrame to list of dictionaries to perform bubble sort
data_list = dataframe.to_dict('records')

# Sort the data using bubble sort based on the 'Price' column
bubble_sort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)
print("Sorted Data:")
print(sorted_dataframe)

plt.subplot(1,2,2)
plt.plot(sorted_dataframe)
plt.ylabel("Data After Sorting Price:")
plt.show()