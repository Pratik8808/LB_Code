#include <iostream>
using namespace std;
template <class T>

void  Reverse( T *arr,int iSize)
{  
    int j=iSize-1;
    for(int i=0;i<j;i++,j--)
    {
      int temp=arr[i];
      arr[i]=arr[j];
      arr[j]=temp;
    }
   
}
int main()
{
    int arr[]={10,20,30,40,50,40,10,50,10,20,10,11};
    Reverse(arr,12);
    for(int i=0;i<12;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
