#include <stdio.h>
void Display()
{
    static int i=1;
    if(i<=4)
    {
        printf("*\t");
        i++;
        Display();
    }
    printf("\n");


}

int main()
{
    Display();
    return 0;
}