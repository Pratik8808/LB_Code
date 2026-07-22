#include <iostream>
template <class T>

T Max(T No1,T No2,T No3)
{
    if(No1>No2 && No1>No3)
    {
        return No1;
    }
    else if(No2>No1 && No2>No3)
    {
        return No2;
    }
    else 
    {
        return No3;
    }

}

int main()
{
    int iRet=Max(10,20,30);
    printf("%d\n",iRet);
    float fRet=Max(10.0f,20.0f,30.5f);
    printf("%f\n",fRet);
    return 0;
   return 0; 
}