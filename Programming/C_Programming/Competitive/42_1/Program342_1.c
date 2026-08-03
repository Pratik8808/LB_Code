#include <stdio.h>
int WhiteSpace(char * arr)
{
    static int Count=0;

    if((*arr)!='\0')
    {
        if((*arr)>'a'  && (*arr)<'z')
        {

            Count++;
        }
        arr++;
       WhiteSpace(arr);
    }
    return Count;
}
int main()
{
   int iRet=0;
   char arr[20];
   printf("Enter the String :");
    scanf("%[^\n]", arr);
   iRet=WhiteSpace(arr);
   printf("%d\n",iRet);
}