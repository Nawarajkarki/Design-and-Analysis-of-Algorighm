// Define the function for merging two sorted arrays
function merge(a, p, q, r) {
    let n1 = q - p + 1;
    let n2 = r - q;
    let list1 = Array(n1 + 1).fill(0);   // Creates an array with n1+1 elements initialized to Zero (0)
    let list2 = Array(n2 + 1).fill(0);   // Creates an array with n2+1 elements initialized to Zero (0)

    for (let i = 0; i < n1; i++) {
        list1[i] = a[p + i];
    }

    for (let j = 0; j < n2; j++) {
        list2[j] = a[q + j + 1];
    }

    list1[n1] = Infinity;   // Assigning infinity to the list[n1]
    list2[n2] = Infinity;
    let i = 0;
    let j = 0;

    for (let k = p; k <= r; k++) {
        if (list1[i] <= list2[j]) {
            a[k] = list1[i];
            i++;
        } else {
            a[k] = list2[j];
            j++;
        }
    }
}

// Define the function for performing merge sort
function mergeSort(a, p, r) {
    if (p < r) {
        let q = Math.floor((p + r) / 2);   // Here Math.floor is used to ensure integer division
        mergeSort(a, p, q);
        mergeSort(a, q + 1, r);
        merge(a, p, q, r);
    }
}

// Define the main function
function main() {
    let my_list = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1,-23 ,34 ,545];
    let n = my_list.length;

    mergeSort(my_list, 0 ,n - 1);
    console.log(my_list);
}

// Call the main function
main();
