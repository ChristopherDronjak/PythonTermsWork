import SelectionSortPractice

def test_unsorted():
    unsorted_list = [20, 34, 25, 12, 22, 11, 99]
    size = len(unsorted_list)
    assert SelectionSortPractice.selectionSort(unsorted_list, size) == [11, 12, 20, 22, 25, 34, 99]

    
def test_sorted():
    sorted_list = [11, 12, 20, 22, 25, 34, 99]
    size = len(sorted_list)
    assert SelectionSortPractice.selectionSort(sorted_list, size) == [11, 12, 20, 22, 25, 34, 99]
    
def test_reverse():
    reverse_list = [99, 34, 25, 22, 20, 12, 11]
    size = len(reverse_list)
    assert SelectionSortPractice.selectionSort(reverse_list, size) == [11, 12, 20, 22, 25, 34, 99]
    
def test_empty():
    empty_list = []
    size = len(empty_list)
    assert SelectionSortPractice.selectionSort(empty_list, size) == []

def test_duplicate():
    duplicate_list = [12, 11, 22, 20, 25, 25, 34, 99]
    size = len(duplicate_list)
    assert SelectionSortPractice.selectionSort(duplicate_list, size) == [11, 12, 20, 22, 25, 25, 34, 99]