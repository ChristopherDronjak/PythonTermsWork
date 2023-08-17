def selectionSort(burger, size):
   
    for step in range(size):
        min_index = step

        for i in range(step + 1, size):
         
            
            if burger[i] < burger[min_index]:
                min_index = i
         
        
        (burger[step], burger[min_index]) = (burger[min_index], burger[step])
    return burger


burger = [-2, 45, 0, 11, -9]
size = len(burger)
selectionSort(burger, size)
print('Sorted Array in Ascending Order:')
print(burger)