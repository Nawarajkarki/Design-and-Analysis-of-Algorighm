package main

import "fmt"

func main() {
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	linear_search(numbers, 6)
}

func linear_search(arr []int, key int) {
	for i := 0; i < len(arr); i++ {
		number := arr[i]
		if number == key {
			fmt.Printf("Key found at %dth index of the array \n", key)
			return
		}
	}
}
