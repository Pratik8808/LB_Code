#include <iostream>
using namespace std;
template <class T>

int  SerachLast( T *arr,int iSize,T iNo)
{   int LastOCc=0;
    for(int i=0;i<iSize;i++)
    {
      if(iNo==arr[i])
      {
        LastOCc=i;
       
      }

    }
   
    return LastOCc+1;
}
int main()
{
    int arr[]={10,20,30,40,50,40,10,50,10,20,10,11};
    int iRet=SerachLast(arr,12,40);
    cout<<iRet<<"\n";
    return 0;
}
