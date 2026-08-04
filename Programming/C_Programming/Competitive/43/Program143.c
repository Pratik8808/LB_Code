#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h> 
#include<string.h>



int CountCapital(char FileName[])
{
    int fd=0;
    fd=open(FileName,O_RDONLY);
    char Buffer[100]={'\0'};
    int iRet=0;
    int iCount=0;

    while(iRet=(read(fd,Buffer,sizeof(Buffer))))
    {
        for(int i=0;i<iRet;i++)
        {
            if(Buffer[i]>'A' && Buffer[i]<'Z')
            {
                iCount++;
            }
        }
        memset(Buffer,'\0',sizeof(Buffer));
    }


    close(fd);

    return iCount;

}

int main()
{
  char FileName[30];
  int iRet=0;
  printf("Enter  the FileName :\n");
  scanf("%s",FileName);
  iRet=CountCapital(FileName);
  printf("%d\n",iRet);

    return 0;
}