
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#define BUFFER_SIZE 1024

void CountChar(char FName[])
{

    int iCount=0;
    int iRet=0;
    char Buffer[BUFFER_SIZE]={'\0'};
    int fd=open(FName,O_RDONLY);
    if(fd==-1)
    {
        printf("Unable to open File\n");
    }
    
    iRet=read(fd,Buffer,13);    
    printf("%s",Buffer);
}

int main()
{   
    char fileName[30];
    char Serach='\0';
    int iRet=0;
    printf("Enter the FileName \n");
    scanf("%[^'\n']s ",fileName);
   
    CountChar(fileName);

    

    return 0;
}