const linear_search = (arr, key) => {
  if (Array.isArray(arr)) {
    const search_length = arr.length; //Avoids calculating array length on each iteration
    for (let index = 0; index < search_length; index++) {
      const number = arr[index];
      if (number === key) {
        console.log(`Key found at ${index}th index of the array`);
        return index;
      }
    }
  } else {
    console.log("Incorrect parameter association");
  }
};

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
linear_search(numbers, 6); //Here we are searching for the key "6"
