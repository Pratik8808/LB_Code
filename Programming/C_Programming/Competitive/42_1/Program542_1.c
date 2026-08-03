#include <stdio.h>
int Reverse(int iNo)
{
    static int Number=0;
    if(iNo!=0)
    {
        int iDigit=iNo%10;
        Number=Number*10+iDigit;
        Reverse(iNo/10);

        
    }

    return Number;
}
int main()
{
   int iRet=0;
   printf("Enter the Number :");
    scanf("%d", &iRet);
   iRet=Reverse(iRet);
   printf("%d\n",iRet);
}