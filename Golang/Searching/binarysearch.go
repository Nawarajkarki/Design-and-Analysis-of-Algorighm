package main

import "fmt"

func binarySearch(arr []int, target int) int {
    left, right := 0, len(arr)-1

    for left <= right {
        mid := left + (right-left)/2

        if arr[mid] == target {
            return mid 
        } else if arr[mid] < target {
            left = mid + 1 
        } else {
            right = mid - 1 
        }
    }

    return -1 
}

func main() {
    sortedArray := []int{1, 3, 5, 7, 9, 11, 13}
    target := 7
    result := binarySearch(sortedArray, target)

    if result != -1 {
        fmt.Printf("Element %d found at index %d\n", target, result)
    } else {
        fmt.Printf("Element %d not found in the array\n", target)
    }
}
