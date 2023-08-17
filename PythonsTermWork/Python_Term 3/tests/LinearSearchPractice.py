
def linear_search(burger, x):
    for index, element in enumerate(burger):
        if element == x:
            return index
    return -1

burger = [3, 6, 2, 8, 4, 1, 7, 5]
x = 6

result = linear_search(burger, x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")