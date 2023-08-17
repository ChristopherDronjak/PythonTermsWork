import pandas as pd
import matplotlib.pyplot as plt

def insertsort(datalist):
    totalnum = len(datalist)
    for i in range(totalnum):
        j = i
        while j > 0 and datalist[j - 1] > datalist[j]:
            datalist[j], datalist[j - 1] = datalist[j - 1], datalist[j]
            j = j - 1
    return datalist

df = pd.read_csv("C:/Users/nzbob/OneDrive/Desktop/Sorting Algorithm Pytest/DiamondValues.csv")
datalist = df['Price'].tolist()
x_val = range(len(datalist))

plt.subplot(1,2,1)
plt.bar(x_val, datalist)
plt.title("Unsorted Plot")

sorted = insertsort(datalist)

plt.subplot(1,2,2)
plt.bar(x_val, sorted, color="green")
plt.title("Insertion Sort Plot")
    
#plt.show()