const numbers = [9, 7, 3, 1, 0, 5, 8, 2, 6, 4];

const bubble_sort = (arr) => {
  if (Array.isArray(arr)) {
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length - 1 - i; j++) {
        if (arr[j] > arr[j + 1]) {
          //if the current value is greater than the value of next index, swap their places
          let swap_variable = arr[j]; //store the arr[j] value somewhere
          arr[j] = arr[j + 1]; //update the arr[j] value with the value of the next index
          arr[j + 1] = swap_variable; //update the arr[j + 1] value with the old value
        }
      }
    }
    console.log(`Array after Bubble sort: ${arr}`);
  } else {
    console.log("Incorrect parameter association");
  }
};

bubble_sort(numbers);
