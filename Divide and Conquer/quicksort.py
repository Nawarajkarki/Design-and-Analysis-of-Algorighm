# Here
#     unsorted_arr  = The unsorted array
#     p             = First index of array
#     r             = Last index of array

def partation(arr, p, r): 

    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]     # Swapping the valuess
    
    arr[i+1], arr[r] = arr[r], arr[i+1]         # Swapping the valuess
    return i + 1



def quicksort(arr, p, r):
    if p < r:
        q  = partation(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, p + 1, r)
    
    return arr


my_list = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1, -23, 34, 545]
n = len(my_list)

quicksort(my_list, 0, n - 1)
print(my_list)
