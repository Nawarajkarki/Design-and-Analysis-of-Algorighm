#include <stdio.h>
void insertionSort(int arr[],int n){
    int i,j,k,key;
    for(i=1;i<=n-1;i++){
        key=arr[i];
        j=i-1;
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=key;
    }
}
int main(){
    int i,n;
    int arr[]={2,8,5,3,2,55,3,32};
    n=sizeof(arr)/sizeof(int);
    insertionSort(arr,n);
    for(i=0;i<n;i++)
        printf("%d\t",arr[i]);
}