#include <stdio.h>
typedef unsigned int UNIT;
// off first 4 bits of Ino
UNIT BitoffFirst4(UNIT iNO)
{
  UNIT iMask=0x01;
  UNIT Count=4;
  for(int i=1;i<=4;i++,Count--)
  {
    UNIT temp=0x01;
    iMask=iMask | (1<<Count-1);

   
  }

  UNIT iResult=(iMask ) | iNO;
  printf("%b\n",iResult);

    return iResult;

}
int main()
{
    int iValue= 0;
    UNIT iRet=0;
    printf("Enter the Number  to of first 4 bit   :");
    scanf("%d",&iValue);
    iRet=BitoffFirst4(iValue);
    printf("The Result of the Number is %d",iRet);



    



}