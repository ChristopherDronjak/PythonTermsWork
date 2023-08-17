def binarySearch(burger, x, low, high):

    while low <= high:
        mid = low + (high - low)//2
        
        if burger[mid] == x:
            return mid
        
        elif burger[mid] < x:
            low = mid + 1
            
        else:
            high = mid - 1
    
    return -1

burger = [3, 5, 8, 10, 12, 15, 17]
x = 12

result = binarySearch(burger, x, 0, len(burger)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")