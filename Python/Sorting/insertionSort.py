def insertionSort(arr, n) -> list:
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

def main():
    my_list=[5,8,7,4,2,9,12,13,11]
    n = len(my_list)
    
    # Make a copy of the original unsorted list
    unsorted_list = my_list.copy()
    
    Sorted_list = insertionSort(my_list, n)
    print(f"UnSorted list/Array {unsorted_list}")
    print(f"Sorted list/Array   {Sorted_list}")


if __name__ == '__main__':
    main()