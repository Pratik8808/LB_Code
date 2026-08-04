#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>


void OpenFile(char FileName[])
{
    int fd=creat(FileName,O_RDONLY);
    if(fd==-1)
    {
        printf("Cannot create File\n");
    }
    else
    {
        printf("File Created in ReadMode only\n");
    }
    
}

int main()
{   char filenam[50];
    printf("Enter the  File Name\n");
    scanf("%s",filenam);
    OpenFile(filenam);
    return 0;
}