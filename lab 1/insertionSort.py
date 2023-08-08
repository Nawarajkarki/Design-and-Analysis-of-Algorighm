def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j+1] = key
    
    return arr


my_list=[5,8,7,4,2,9,12,13,11]
print(f"UnSorted list/Array {my_list} ")
Sorted_list = insertionSort(my_list)
print(f"Sorted list/Array   {Sorted_list} ")
