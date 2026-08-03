#include <stdio.h>
int LargestX(int S)
{
    static int LargestNumber=0;
    if(S!=0)
    {
        int iDigit=S%10;
        if(LargestNumber<iDigit)
        {
            LargestNumber=iDigit;
        }
        LargestX(S/10);
    }

    return LargestNumber;
}
int main()
{
   int iRet=0;
   printf("Enter the String :");
    scanf("%d", &iRet);
   iRet=LargestX(iRet);
   printf("%d\n",iRet);
}