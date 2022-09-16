"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(arr, l ,h):
    pivot = arr[h]
    i = l -1
    for j in range(l,h):
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i+1]
    return i + 1
    
def quicksort(array, low, high):

    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi -1)
        quicksort(array, pi +1, high)
    return(array)
    
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test, 0, len(test) -1))