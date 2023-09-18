package main

import "fmt"

func bubble_sort(arr []int) {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr)-1-i; j++ {
			if arr[j] > arr[j+1] {
				//if the current value is greater than the value of next index, swap their places
				swap_variable := arr[j] //store the arr[j] value somewhere
				arr[j] = arr[j+1]       //update the arr[j] value with the value of the next index
				arr[j+1] = swap_variable //update the arr[j + 1] value with the old value
			}
		}
	}
	fmt.Printf("Array after Bubble sort: %v\n", arr)
}

func main() {
	numbers := []int{9, 7, 3, 1, 0, 5, 8, 2, 6, 4}
	bubble_sort(numbers)
}
