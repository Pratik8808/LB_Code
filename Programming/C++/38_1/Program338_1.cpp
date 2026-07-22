#include <iostream>
using namespace std;
template <class T>

int  FirstFrequency( T *arr,int iSize,T iNo)
{   int FirstOccurence=0;
    for(int i=0;i<iSize;i++)
    {
      if(iNo==arr[i])
      {
        FirstOccurence=i;
        break;
      }

    }
   
    return FirstOccurence+1;
}
int main()
{
    int arr[]={10,20,30,40.5,50,40,10,50,10,20,10,11};
    int iRet=FirstFrequency(arr,12,40);
    cout<<iRet<<"\n";
    return 0;
}
