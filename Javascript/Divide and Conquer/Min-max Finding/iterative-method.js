// Define the function for finding the minimum and maximum elements in an array
function minMax(myList, len) {
    let min = myList[0];
    let max = myList[0];

    for (let i = 1; i < len; i++) {
        if (myList[i] > max) {
            max = myList[i];
        }
        if (myList[i] < min) {
            min = myList[i];
        }
    }

    return [min, max];
}

// Define the main function
function main() {
    let myList = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1, -23, 34, 545];
    let n = myList.length;

    let [min, max] = minMax(myList, n);
    console.log(`min = ${min}, max = ${max}`);
}

// Call the main function
main();
