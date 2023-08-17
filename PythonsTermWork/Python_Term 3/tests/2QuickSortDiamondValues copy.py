from matplotlib import pyplot as plt
import pandas as pd

def Qsort (value):

    if len(value)<= 1:

        return value

    pivot = value[len(value) // 2]
    left = [x for x in value if x < pivot]
    middle = [x for x in value if x == pivot]
    right = [x for x in value if x > pivot]
    
    return Qsort(left) + middle + Qsort(right)

column = 'Price'
filepath = "C:/Users/nzbob/OneDrive/Desktop/Python_Term 3/DiamondValues.csv"
df = pd.read_csv(filepath)

unsorted_data = df[column].tolist()
sorted_data = Qsort(unsorted_data)

print(sorted_data)