#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include  <unistd.h>
# define BUFFER_SIZE 1024
int Display(char  FileName[],char stringp[])
{
    int iCount=0;
    int fd=open(FileName,O_RDWR|O_APPEND);
    char Buffer[BUFFER_SIZE]={'\0'};
    int iRet=0;
  
    write(fd,stringp,strlen(stringp));
    close(fd);
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
   int iRet=Display(FileName,string);
   printf("%d\n",iRet);


    return 0;
}