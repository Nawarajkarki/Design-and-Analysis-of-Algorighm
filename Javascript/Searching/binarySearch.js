// Import the readline module
const readline = require('readline');

// Create a readline interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Define the function for linear search
function linearSearch(my_list, key) {
    // Initialize the lower and upper bounds of the search
    let low = 0;
    let high = my_list.length - 1;

    // Continue searching as long as there is a range to search within
    while (low <= high) {
        // Calculate the middle index
        let mid = Math.floor((low + high) / 2);

        // If the key is found, return its index
        if (key === my_list[mid]) {
            return mid;
        }
        // If the key is less than the middle element, search in the left half
        else if (key < my_list[mid]) {
            high = mid - 1;
        }
        // If the key is greater than the middle element, search in the right half
        else {
            low = mid + 1;
        }
    }

    // If the key is not found, return -1
    return -1;
}

// Initialize the array
let my_list = [1, 4, 8, 11, 17, 29, 35, 37, 44, 61];

// Ask for the key to be searched
rl.question('Enter key to be searched: ', (key) => {
    // Perform linear search on the array for the given key
    let flag = linearSearch(my_list, Number(key));

    // Print whether or not the key was found and its position if it was found
    if (flag === -1) {
        console.log("Search key is not found");
    } else {
        console.log(`Search key is found at position ${flag}`);
    }

    // Close the readline interface
    rl.close();
});
