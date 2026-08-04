#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#define BUFFER_SIZE 1024

int CountChar(char FName[],char Character)
{

    int iCount=0;
    int iRet=0;
    int fd=open(FName,O_RDONLY);
    if(fd==-1)
    {
        return -1;
    }
    char Buffer[BUFFER_SIZE]={'\0'};
    while((iRet=read(fd,Buffer,sizeof(Buffer) )))
    {
        for(int i=0;i<iRet;i++)
        {
            if(Buffer[i]==Character)
            {
                iCount++;
            }
        }
        memset(Buffer,'\0',sizeof(Buffer));
    }

    return iCount;
}

int main()
{   
    char fileName[30];
    char Serach='\0';
    int iRet=0;
    printf("Enter the FileName \n");
    scanf("%[^'\n']s ",fileName);
    printf("Enter the Character to serach \n");
    scanf(" %c",&Serach);
    iRet=CountChar(fileName,Serach);
    printf("Number of Charceter %c  is :%d\n",Serach,iRet);

    return 0;
}