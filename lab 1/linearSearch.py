def linearSearch(arr):
    key = int(input("Enter the search item:- ")) # Search Item 
    n = len(arr)
    for i in range(n):
        if arr[i] == key: 
            print(f"Key found at {i}th index")
            return 

    print("key not found")
    

arr=[5,8,7,4,2,9,12,13,11]
linearSearch(arr)

