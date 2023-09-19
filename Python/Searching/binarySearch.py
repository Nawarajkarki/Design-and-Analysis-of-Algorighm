# Define the function for linear search
def linear_search(my_list, key):
    # Initialize the lower and upper bounds of the search
    low = 0
    high = len(my_list) - 1

    # Continue searching as long as there is a range to search within
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # If the key is found, return its index
        if key == my_list[mid]:
            return mid
        # If the key is less than the middle element, search in the left half
        elif key < my_list[mid]:
            high = mid - 1
        # If the key is greater than the middle element, search in the right half
        else:
            low = mid + 1

    # If the key is not found, return -1
    return -1

# Define the main function
def main():
    # Initialize the array and the key to be searched
    my_list = [1, 4, 8, 11, 17, 29, 35, 37, 44, 61]
    key = int(input("Enter key to be searched:\t"))

    # Perform linear search on the array for the given key
    flag = linear_search(my_list, key)

    # Print whether or not the key was found and its position if it was found
    if flag == -1:
        print("Search key is not found")
    else:
        print(f"Search key is found at position {flag}")

# Call the main function
if __name__ == "__main__":
    main()
