#include<stdio.h>
int heapsize;
int length;
void swap(int *a,int *b){
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
void maxHeap(int arr[],int i){
    int l,r,largest;
    l=2*i+1;
    r=2*i+2;
    if(l<=heapsize-1 && arr[l]>arr[i]){
        largest=l;
    }
    else{
        largest=i;
    }
    if(r<=heapsize-1 && arr[r]>arr[largest]){
        largest=r;
    }
    if(largest!=i){
        swap(&arr[i],&arr[largest]);
        maxHeap(arr,largest);
    }
}
    void buildHeap(int arr[]){
        int i;
        heapsize=length;
        for(i=(length/2)-1;i>=0;i--){
            maxHeap(arr,i);
        }
    }
    void heapSort(int arr[]){
        int i;
        buildHeap(arr);
        printf("After build max heap:\t");
        for(i=0;i<length;i++){
            printf("%d\t",arr[i]);
        }
        printf("\n");
        for(i=length-1;i>=1;i--){
            swap(&arr[0],&arr[i]);
            heapsize=heapsize-1;
            maxHeap(arr,0);
        }
    }
    int main(){
        int i;
        int arr[]={8, 9, 2, 5, 7, 1, 19};
        length=sizeof(arr)/sizeof(int);
        heapSort(arr);
        printf("After heap sort:\t");
        for(i=0;i<length;i++)
            printf("%d\t",arr[i]);
        printf("\n");
    }
