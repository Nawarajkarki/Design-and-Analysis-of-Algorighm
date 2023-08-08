from common import swap

def bubbleSort(arr, n):
    for key in range(1, n):
        issort = 1
        for i in range(n-key):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = swap(arr[i], arr[i+1])
                issort = 0
        
        if issort == 1:
            break
    
    return arr



my_list = [5,8,7,4,2,9,12,13,11]
n = len(my_list)

print(f"UnSorted list/Array {my_list} ")
Sorted_list = bubbleSort(my_list, n)
print(f"Sorted list/Array   {Sorted_list}")