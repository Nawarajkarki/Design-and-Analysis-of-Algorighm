// Define the function for partitioning the array
function partition(arr, p, r) {
    let x = arr[r];
    let i = p - 1;

    for (let j = p; j < r; j++) {
        if (arr[j] <= x) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];  // Swapping the values
        }
    }

    [arr[i+1], arr[r]] = [arr[r], arr[i+1]];  // Swapping the values
    return i + 1;
}

// Define the function for performing quicksort
function quicksort(arr, p, r) {
    if (p < r) {
        let q = partition(arr, p, r);
        quicksort(arr, p, q - 1);
        quicksort(arr, q + 1, r);
    }

    return arr;
}

// Define the main function
function main() {
    let my_list = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1, -23, 34, 545];
    let n = my_list.length;

    quicksort(my_list, 0, n - 1);
    console.log(my_list);
}

// Call the main function
main();
