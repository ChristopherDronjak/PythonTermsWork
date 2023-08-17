def insertionSort(burger):
    
    for step in range(1, len(burger)):
        key = burger[step]
        x = step - 1
        
        while x >= 0 and key < burger[x]:
            burger[x + 1] = burger[x]
            x = x - 1
            
        burger[x + 1] = key
    return burger

burger = [9, 5, 1, 4, 3]
insertionSort(burger)
print('Sorted Array in Ascending Order:')
print(burger)


