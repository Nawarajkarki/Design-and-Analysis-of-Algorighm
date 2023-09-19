function insertionSort(arr) {
    let n = arr.length;
    for (let i = 1; i < n; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
    return arr;
}

function main() {
    let my_list=[5,8,7,4,2,9,12,13,11];
    
    // Make a copy of the original unsorted list
    let unsorted_list = [...my_list];
    
    let sorted_list = insertionSort(my_list);
    console.log("UnSorted list/Array", unsorted_list);
    console.log("Sorted list/Array  ", sorted_list);
}

main();
