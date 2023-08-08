from common import swap

def selectionSort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n, +1):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] =  swap(arr[min_idx], arr[i])

    return arr



my_list=[5,8,7,4,2,9,12,13,11]
n = len(my_list)


print(f"UnSorted list/Array {my_list} ")
Sorted_list = selectionSort(my_list, n)
print(f"Sorted list/Array   {Sorted_list}")
