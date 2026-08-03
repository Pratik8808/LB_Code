#include <stdio.h>

void Display(int iNo)
{
    static char cRet='A';
    if(iNo>=1)
    {
        printf("%c\t",cRet);
        cRet++;
        Display(iNo-1);
    }

}
int main()
{   int iValue=0;
    printf("Enter Number\n");
    scanf("%d",&iValue);
    Display(iValue);
    

    return 0;
}