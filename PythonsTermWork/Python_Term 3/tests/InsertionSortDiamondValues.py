import pandas as pd

def insertionSort(arr):
    
    for step in range(1, len(arr)):
        key = arr[step]
        x = step - 1
        
        while x >= 0 and key['Price'] < arr[x]['Price']:
            arr[x + 1] = arr[x]
            x = x - 1
            
        arr[x + 1] = key

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
insertionSort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Sorted Data:")
print(sorted_dataframe)