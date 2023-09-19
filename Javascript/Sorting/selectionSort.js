function selectionSort(arr) {
    let n = arr.length;
    // One by one move boundary of unsorted subarray
    for (let i = 0; i < n-1; i++) {
        // Find the minimum element in unsorted array
        let min_idx = i;
        for (let j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        // Swap the found minimum element with the first element of unsorted array
        let temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
    return arr;
}

function main() {
    let my_list=[5,8,7,4,2,9,12,13,11];
    // Make a copy of the original unsorted list
    let unsorted_list = [...my_list];

    let sorted_list = selectionSort(my_list);
    console.log("UnSorted list/Array", unsorted_list);
    console.log("Sorted list/Array  ", sorted_list);
}

main();
