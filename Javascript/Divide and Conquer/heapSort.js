// Define the function for swapping two elements
function swap(a, b) {
    return [b, a];
}

// Define the function for maintaining the max heap property
function maxHeap(arr, i, heapsize) {
    let l = 2 * i + 1;
    let r = 2 * i + 2;
    let largest;

    if (l <= heapsize - 1 && arr[l] > arr[i]) {
        largest = l;
    } else {
        largest = i;
    }

    if (r <= heapsize - 1 && arr[r] > arr[largest]) {
        largest = r;
    }

    if (largest !== i) {
        [arr[i], arr[largest]] = swap(arr[i], arr[largest]);
        maxHeap(arr, largest, heapsize);
    }
}

// Define the function for building a max heap
function buildHeap(arr) {
    let length = arr.length;
    let heapsize = length;

    for (let i = Math.floor(length / 2) - 1; i >= 0; i--) {
        maxHeap(arr, i, heapsize);
    }
}

// Define the function for performing heap sort
function heapSort(arr) {
    buildHeap(arr);
    console.log("After build max heap:\t", ...arr);

    let length = arr.length;
    let heapsize = length;

    for (let i = length - 1; i > 0; i--) {
        [arr[0], arr[i]] = swap(arr[0], arr[i]);
        heapsize -= 1;
        maxHeap(arr, 0, heapsize);
    }
}

// Define the main function
function main() {
    let arr = [8, 9, 2, 5, 7, 1, 19];
    heapSort(arr);
    console.log("After heap sort:\t", ...arr);
}

// Call the main function
main();
