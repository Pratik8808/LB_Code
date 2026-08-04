#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include  <unistd.h>
# define BUFFER_SIZE 1024
int Display(char  FileName[])
{
    int iCount=0;
    int fd=open(FileName,O_RDONLY);
    char Buffer[BUFFER_SIZE]={'\0'};
    int iRet=0;
  
    while(iRet=read(fd,Buffer,sizeof(Buffer)))
    {
        iCount=iCount+iRet;
        memset(Buffer,'\0',sizeof(Buffer));
    }
    return iCount;
}

int main()
{
   char FileName[30];
    char string[30];
   printf("Enter the File Name\n");
   scanf("%s",FileName);
   printf("Enter the String \n");
   scanf("%s",string);
   int iRet=Display(FileName);
   printf("%d\n",iRet);


    return 0;
}