#include <stdio.h>

// Global valriables to store Min & Max values
int min;
int max;


// Function to find the min and max values 
void min_max(int arr[], int i, int j){
    int min1, max1;

// If the array has only one element
    if(i == j){
        max = min = arr[i];
   }

// If the array has two elements
    else if (i == j-1){
        if (arr[i] < arr[j]){
            max = arr[j];
            min = arr[i];
        }
        else{
            max = arr[i];
            min = arr[j];
        }
   }

// If the array has more than two elements.
    else{
        int mid;

//      Recursively Find Minimum and Maximum values in the first half
        mid = (i+j)/2;
        min_max(arr, i, mid);
        max1 = max;
        min1 = min;


//      Recursively Find Minimum and Maximum values in the second half
       min_max(arr, mid+1, j);
    //    Update the Global min and max
        if (max < max1)
            max = max1;
        if (min > min1)
            min = min1;
    }
}


int main(){
    int i, j;

    // Initiallize an array
    int arr[] = {2, 23, 45, 56,4,56,325,6,445};
    j = sizeof(arr)/sizeof(int);          //  This gives the length of our array.  

// min_max function call with (array, first_index, last_index)
    min_max(arr, 0, j-1);
    printf("min = %d, max = %d", min, max);
}