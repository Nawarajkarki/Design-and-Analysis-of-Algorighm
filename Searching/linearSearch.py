def linearSearch(arr,n):
    key = int(input("Enter the search item:- ")) # Search Item 
    for i in range(n):
        if arr[i] == key: 
            print(f"Key found at {i}th index")
            return 

    print("key not found")
    
arr=[5,8,7,4,2,9,12,13,11]
n = len(arr)
linearSearch(arr,n)

