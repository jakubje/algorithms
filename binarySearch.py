"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    lower_index = 0
    upper_index = len(input_array) - 1
    while lower_index <= upper_index:
        mid = int((lower_index + upper_index) / 2)
        if input_array[mid] < value:
            lower_index = mid + 1
        elif input_array[mid] > value:
            upper_index = mid - 1
        else:
            return mid
    return -1

test_list = [1, 3, 9, 11, 15, 19, 29, 31, 65]
test_val1 = 28
test_val2 = 11
test_val3 = 3
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))
print (binary_search(test_list, test_val3))
