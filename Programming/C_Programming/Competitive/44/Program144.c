#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>


void OpenFile(char FileName[])
{
    int fd=open(FileName,O_RDONLY);
    printf("%d",fd);
    if(fd==-1)
    {
        printf("Unable to open FIlename\n");
    }
    else{

        printf("File Opened Sucessfully\n");
    }
}

int main()
{   char filenam[50];
    printf("Enter the  File Name\n");
    scanf("%s",filenam);
    OpenFile(filenam);
    return 0;
}