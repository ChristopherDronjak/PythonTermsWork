import pandas as pd
import b_sort
import time

#pytest -s

df = pd.read_csv("C:/Users/nzbob/OneDrive/Desktop/Sorting Algorithm Pytest/DiamondValues.csv")
datalist = df["Price"].tolist()
sorted_datalist = sorted(datalist)   
 
def test_sorted():
    #sorted == sorted
    start = time.time()
    assert b_sort.bubblesort(sorted_datalist) == sorted_datalist
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")

def test_unsorted():
    #function(unsorted) == sorted
    start = time.time()
    assert b_sort.bubblesort(datalist) == sorted_datalist
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")
    
def test_empty():
    nolist = []
    start = time.time()
    assert b_sort.bubblesort(nolist) == []
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")

def test_reversed():
    #a reversed sorted data == sorted
    reverse_list = sorted(datalist)
    reverse_list.reverse()
    start = time.time()
    assert b_sort.bubblesort(reverse_list) == sorted_datalist
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")

def test_duplicate():
    #duplicate unsorted == duplicate sorted
    duplicate = datalist * 2
    start = time.time()
    assert b_sort.bubblesort(duplicate) == sorted(duplicate)
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")
