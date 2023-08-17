def bubbleSort(burger):
    y = len(burger)
    
    for i in range(y):
        
        for j in range(0, y-i-1):
            
            if burger[j] > burger[j+1]:
                burger[j], burger[j+1] = burger[j+1], burger[j]
    return burger

if __name__ == "__main__":
    burger = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", burger)
    
    bubbleSort(burger)
    print("Sorted array:", burger)