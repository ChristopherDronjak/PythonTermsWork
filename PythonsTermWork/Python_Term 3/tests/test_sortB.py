import BubbleSortPractice

def test_unsorted():
    unsorted_list = [20, 34, 25, 12, 22, 11, 99]
    assert BubbleSortPractice.bubbleSort(unsorted_list) == [11, 12, 20, 22, 25, 34, 99]
    
def test_sorted():
    sorted_list = [11, 12, 20, 22, 25, 34, 99]
    assert BubbleSortPractice.bubbleSort(sorted_list) == [11, 12, 20, 22, 25, 34, 99]
    
def test_reverse():
    reverse_list = [99, 34, 25, 22, 20, 12, 11]
    assert BubbleSortPractice.bubbleSort(reverse_list) == [11, 12, 20, 22, 25, 34, 99]
    
def test_empty():
    empty_list = []
    assert BubbleSortPractice.bubbleSort(empty_list) == []

def test_duplicate():
    duplicate_list = [12, 11, 22, 20, 25, 25, 34, 99]
    assert BubbleSortPractice.bubbleSort(duplicate_list) == [11, 12, 20, 22, 25, 25, 34, 99]