#include<stdio.h>
void linearSearch(int arr[],int n,int key){
int i,flag=0,pos;
for(i=0;i<n;i++){
    if(arr[i]==key){
        flag=1;
        pos=i;
        break;
    }
}
if(flag){
    printf("searched key is present at position %d\n",pos);
}
else{
    printf("searched  key is not found");
}
}
int main(){
int n,key;
int arr[]={4,7,9,2,3,6,44};
n=sizeof(arr)/sizeof(int);
printf("enter key to be searched:\t");
scanf("%d",&key);
linearSearch(arr,n,key);
}