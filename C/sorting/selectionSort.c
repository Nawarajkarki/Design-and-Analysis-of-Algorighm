#include <stdio.h>
void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
void selectionSort(int arr[], int n)
{
    int least, p, i, j;
    for (i = 0; i <=n-1; i++)
    {
        least = arr[i];
        p = i;
        for (j = i + 1; j <= n-1; j++)
        {
            if (arr[j] < least)
            { // Compare with 'least' instead of 'arr[i]'
                least = arr[j];
                p = j;
            }
            
        }
int temp;
temp=arr[i];
arr[i]=arr[p];
arr[p]=temp;
        // swap(&arr[i], &arr[p]);
        int k=0;
            for (k=0; k < n; k++)
            {
                printf("%d\t", arr[k]);
            }
            printf("\n");
    }
}

int main()
{
    int i, n;
    int arr[] = {6, 2, 9, 3, 100, 32};
    n = sizeof(arr) / sizeof(int);
    selectionSort(arr, n);
    for (i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
}