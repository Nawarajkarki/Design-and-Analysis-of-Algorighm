def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Input 10 numbers from the user
arr = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print("Original array:", arr)

sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
