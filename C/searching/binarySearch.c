#include<stdio.h>
int linearSearch(int arr[],int n,int key){
int low=0,high=n-1;
while(low<=high){
    int mid=(low+high)/2;
    if(key==arr[mid]){
        return mid;
    }
    else if(key<arr[mid]){
        high=mid-1;
    }
    else{
        low=mid+1;
    }
}
return -1;
}
int main(){
int n,key;
int arr[]={1,2,3,4,7,9,15,67};
n=sizeof(arr)/sizeof(int);
printf("enter key to be searched:\t");
scanf("%d",&key);
int flag=linearSearch(arr,n,key);
if(flag==-1){
    printf("search key is not found");
}
else{
    
    printf("search key is found at position %d\n",flag);

}
}