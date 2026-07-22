#include <iostream>
using namespace std;
template <class T>

int  Frequency( T *arr,int iSize,T iNo)
{   int iCount=0;
    for(int i=0;i<iSize;i++)
    {
      if(iNo==arr[i])
      {
        iCount++;
      }

    }
   
    return iCount;
}
int main()
{
    int arr[]={10,20,30,40,50,40,10,50,10,20,10,11};
    int iRet=Frequency(arr,12,10);
    cout<<iRet<<"\n";
    return 0;
}
