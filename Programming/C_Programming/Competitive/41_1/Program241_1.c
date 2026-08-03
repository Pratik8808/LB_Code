#include <stdio.h>
void Display(int n)
{   if(n>0)
    {

        printf("%d \t* \t",n);
        Display(n-1);
    }
}

int main()
{
    Display(5);

    return 0;
}