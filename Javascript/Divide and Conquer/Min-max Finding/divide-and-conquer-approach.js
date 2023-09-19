// Define the function for finding the minimum and maximum elements in an array using divide and conquer
function minMax(myList, p, r) {
    let min;
    let max;

    if (p === r) {
        max = min = myList[p];
    } else if (p === r - 1) {
        if (myList[p] < myList[r]) {
            max = myList[r];
            min = myList[p];
        } else {
            max = myList[p];
            min = myList[r];
        }
    } else {
        // Divide the problem in half
        let mid = Math.floor((p + r) / 2);   // Integer division

        let [min1, max1] = minMax(myList, p, mid);

        [min, max] = minMax(myList, mid + 1, r);
        if (max1 > max) {
            max = max1;
        }
        if (min1 < min) {
            min = min1;
        }
    }

    return [min, max];
}

// Define the main function
function main() {
    let myList = [5, 8, 7, 4, 2, 9, 12, 13, 11, 23, 1, -1,-23 ,34 ,545];
    let l = myList.length;

    let [min,max] = minMax(myList ,0 ,l-1);
    console.log(`min = ${min}, max = ${max}`);
}

// Call the main function
main();
