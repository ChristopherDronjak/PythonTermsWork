import pandas as pd

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        # current index is the min value
        min_idx = i
        for j in range(i + 1, n):
            # index of the minimum value in the unsorted part of the list
            if arr[j]['Price'] < arr[min_idx]['Price']:
                min_idx = j

        # Swap the found minimum value with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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

# Convert DataFrame to list of dictionaries to perform selection sort
data_list = dataframe.to_dict('records')

# Sort the data using selection sort based on the 'Price' column
selectionSort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Sorted Data:")
print(sorted_dataframe)