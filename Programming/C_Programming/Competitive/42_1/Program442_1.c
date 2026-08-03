#include <stdio.h>
int SmallestX(int S)
{
    static int SmallestNumber=0;
    if(S!=0)
    {
        int iDigit=S%10;
        if(SmallestNumber>iDigit)
        {
            SmallestNumber=iDigit;
        }
        SmallestX(S/10);
    }

    return SmallestNumber;
}
int main()
{
   int iRet=0;
   printf("Enter the String :");
    scanf("%d", &iRet);
   iRet=SmallestX(iRet);
   printf("%d\n",iRet);
}