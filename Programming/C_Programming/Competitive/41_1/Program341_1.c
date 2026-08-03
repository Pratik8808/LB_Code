#include <stdio.h>
int Strlenx(char * arr)
{
    static int Count=0;

    if((*arr)!='\0')
    {
       arr++;
       Count++;
      
       Strlenx(arr);
    }
    return Count;
}
int main()
{
   int iRet=0;
   char arr[20];
   printf("Enter the String :");
   scanf("%s",arr);
   iRet=Strlenx(arr);
   printf("%d\n",iRet);
}