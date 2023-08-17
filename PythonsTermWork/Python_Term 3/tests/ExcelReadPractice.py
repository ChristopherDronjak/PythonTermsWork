import pandas as pd

def read_excel(filepath, column):
    dataframe = pd.read_excel(filepath, usecols = column)
    return dataframe
#Vars
column = [1, 4]
filepath = 'C:/Users/nzbob/OneDrive/Desktop/Python_Term 3/PracticeExcel.xlsx' 
dataframe = read_excel(filepath, column)
print(dataframe)
print("")
sorted_date = dataframe.sort_values(by='Percentage')
print("Sorted Data: ")
print(sorted_date)