import pandas as pd

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x['Price'] < pivot]
        right = [x for x in arr if x['Price'] >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

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

# Convert DataFrame to list of dictionaries to perform bubble sort
data_list = dataframe.to_dict('records')

# Sort the data using bubble sort based on the 'Price' column
quicksort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Sorted Data:")
print(sorted_dataframe)