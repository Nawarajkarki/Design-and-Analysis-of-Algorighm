#include <stdio.h>

void min_max(int arr[], int l, int *min, int *max){
    *max = arr[0];
    *min = arr[0];

    for(int i=1; i<l; i++){
        if(arr[i] > *max){
            *max = arr[i];
        }
        if(arr[i] < *min){
            *min = arr[i];
        }
    }
}

int main(){
    int min, max;

    // Initialize an array
    int arr[] = {2, 23, 45, 5, 334, 34, 324,6,4,56,325,6,445};
    int j = sizeof(arr)/sizeof(int);          //  This gives the length of our array.  

    // min_max function call with (array, first_index, last_index)
    min_max(arr, j, &min, &max);
    printf("min = %d, max = %d", min, max);
}
