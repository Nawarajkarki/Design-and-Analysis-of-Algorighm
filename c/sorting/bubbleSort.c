#include<stdio.h>
void swap(int *a, int *b){
    int temp;
    temp=*a;
   *a=*b;
   *b=temp;
}
void bubbleSort(int arr[],int n){
   int i,j;
   for(i=0;i<n-1;i++){
    for(j=0;j<n-i-1;j++){
        if(arr[j]>arr[j+1])
        swap(&arr[j],&arr[j+1]);
    }
       int k=0;
       for(k=0;k<n;k++)
   printf("%d\t",arr[k]);
   printf("\n");

   }
   }
int main(){
int i,n;
    int arr[]={25,57,48,37,12,92,86,33};
    n=sizeof(arr)/sizeof(int);
    bubbleSort(arr,n);
    
}