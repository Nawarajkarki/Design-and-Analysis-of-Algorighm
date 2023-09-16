def bubbleSort(arr, n) -> list:
    for key in range(1, n):
        issort = 1
        for i in range(n-key):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                issort = 0
        if issort == 1:
            break
    return arr

my_list = [5,8,7,4,2,9,12,13,11]
n = len(my_list)

# Make a copy of the original unsorted list
unsorted_list = my_list.copy()

Sorted_list = bubbleSort(my_list, n)
print(f"UnSorted list/Array {unsorted_list}")
print(f"Sorted list/Array   {Sorted_list}")