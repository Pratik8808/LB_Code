#include <iostream>
template <class T>

T Max(T *arr, int iSize)
{
    T Max=arr[0];
    int i=0;
    for(i=0;i<iSize;i++)
    {
        if(Max<arr[i])
        {
            Max=arr[i];
        }
    }
    return Max;
}

int main()
{
    int arr[]={10,20,30,40,50};
    float brr[]={10.0f,3.7f,9.8f,8.7f};
    int iMax=Max(arr,5);
    float fMax=Max(brr,4);

    printf("%d\n",iMax);
    printf("%f\n",fMax);

   return 0; 
}