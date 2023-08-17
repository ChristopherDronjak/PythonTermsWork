import pandas as pd
import matplotlib.pyplot as plt
import random

def swap(datalist, i, j):
    temp = datalist[i]
    datalist[i] = datalist[j]
    datalist[j] = temp

def partition(datalist, lo, hi):
    r = random.randint(lo, hi)
    datalist[lo], datalist[r] = datalist[r], datalist[lo]
    
    pivot = datalist[lo]
    (i, j) = (lo - 1, hi + 1)
    
    while True:
        while True:
            i += 1
            if datalist[i] >= pivot:
                break
        while True:
            j -= 1
            if datalist[j] <= pivot:
                break
        if i >= j:
            return j
        swap(datalist, i, j)

def qsort(datalist, lo, hi):
    if lo >= hi:
        return
    pivot = partition(datalist, lo, hi)
    qsort(datalist, lo, pivot)
    qsort(datalist, pivot + 1, hi)
    
def quicksort(datalist) -> list:
    qsort(datalist, 0, len(datalist) - 1)
    return datalist
    
df = pd.read_csv("C:/Users/nzbob/OneDrive/Desktop/Sorting Algorithm Pytest/DiamondValues.csv")
datalist = df['Price'].tolist()

x_val = range(len(datalist))
plt.subplot(1,2,1)
plt.bar(x_val, datalist)
plt.title("Unsorted Plot")

sorted = quicksort(datalist)

plt.subplot(1,2,2)
plt.bar(x_val, sorted, color="green")
plt.title("Quick Sort Plot")
    
#plt.show()