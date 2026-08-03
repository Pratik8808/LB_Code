#include <stdio.h>
void Display()
{
    
static  int i=1;
static char cRet='a';
if(i<=6)
{
    printf("%c\t",cRet);
    i++;
    cRet++;
    Display();
}
    


}

int main()
{
    Display();
    return 0;
}