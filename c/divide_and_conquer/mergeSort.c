#include <stdio.h>
#include<limits.h>
void merge(int arr[], int p, int q, int r) {
    int n1, n2, i, j, k;
    n1 = q - p + 1;
    n2 = r - q;
    int lLength = n1 + 1;
    int rLength = n2 + 1;
    int L[lLength];
    int R[rLength];
    n1 = q - p + 1;
    n2 = r - q;
    for (i = 0; i < n1; i++) {
        L[i] = arr[p + i];  // Corrected index
    }
    for (j = 0; j < n2; j++) {
        R[j] = arr[q + j + 1];  // Corrected index
    }
    L[n1] = INT_MAX;
    R[n2] = INT_MAX;
    i = 0;  // Initialize i with 0 instead of 1
    j = 0;
    for (k = p; k <= r; k++) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i = i + 1;
        } else {
            arr[k] = R[j];
            j = j + 1;
        }
    }
    
}

void mergeSort(int arr[], int p, int r) {
    int q;
    if (p < r) {
        q = (p + r) / 2;
        mergeSort(arr, p, q);
        mergeSort(arr, q + 1, r);
        merge(arr, p, q, r);
    }
}

int main() {
    int n;
    int arr[] = {3, 9, 1, 6, 8, 4, 73, 34};
    n = sizeof(arr) / sizeof(int);
    int i;
    mergeSort(arr, 0, n - 1);  // Pass n - 1 as r
    for (i = 0; i < n; i++) {
        printf("%d\t", arr[i]);
    }
    return 0;
}