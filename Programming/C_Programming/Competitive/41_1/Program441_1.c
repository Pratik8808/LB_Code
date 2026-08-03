#include <stdio.h>


int factorial(int iNo)
{
    static int  fact=1;
    if(iNo>=1)
    {
        fact=fact*iNo;
        factorial(iNo-1);
    }
    return fact;
}
int main()
{   int iValue=0;
    printf("Enter Number\n");
    scanf("%d",&iValue);
    int iRet=factorial(iValue);
    printf("%d\n",iRet);

    return 0;
}