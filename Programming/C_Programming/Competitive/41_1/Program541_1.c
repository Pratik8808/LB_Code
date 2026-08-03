#include <stdio.h>


int Mult(int iNo)
{
    static int  fact=1;
    
    if(iNo !=0)
    {   int Digit=iNo%10;
        fact=fact*Digit;
        Mult(iNo/10);
    }
    return fact;
}
int main()
{   int iValue=0;
    printf("Enter Number\n");
    scanf("%d",&iValue);
    int iRet=Mult(iValue);
    printf("%d\n",iRet);

    return 0;
}