#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#define BUFFER_SIZE 1024

int WhiteSpace(char FName[])
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
            if(Buffer[i]==' ')
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
    printf("Enter the FileName \n");
    scanf("%s",fileName);
    int iRet=WhiteSpace(fileName);
    printf("Number of Space is %d\n",iRet);

    return 0;
}