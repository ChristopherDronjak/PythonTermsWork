def quicksort(burger):
    if len(burger) <= 1:
        return burger
    else:
        pivot = burger[0]
        left = [x for x in burger[1:] if x < pivot]
        right = [x for x in burger[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

burger = [1, 7, 4, 1, 10, 9, -2]
sortedarray = quicksort(burger)
print("Sorted Array in Ascending Order:")
print(sortedarray)

