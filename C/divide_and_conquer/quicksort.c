#include <stdio.h>
#include<conio.h>
void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int A[],int p,int r){
int i,x;
x=A[r];
i=p-1;
for(int j=p;j<=r-1;j++){
    if(A[j]<=x)
    i=i+1;
    swap(A[i],A[j]);
}
sweap(A[i+1],A[r]);
return i+1;
}
void quicksort(int arr[], int p, int r) {
    if (p < r) {
        int q = partition(arr, p, r);
        quicksort(arr, p, q - 1);
        quicksort(arr, q + 1, r);
    }
}

int main() {
    int i, n;
     printf("Quicksort");
    int arr[] = {5, 1, 33, 12, 3, 2, 73};
     
    n = sizeof(arr) / sizeof(int);
    printf("Quicksort");
    quicksort(arr, 0, n - 1);
    for (i = 0; i < n; i++) {
        printf("%d\t", arr[i]);
    }

}
