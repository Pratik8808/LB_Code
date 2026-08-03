#include <stdio.h>
void Display(int iNo)
{
    static int i=1;
    if(i<=5)
    {
        printf("%d\t",i);
        i++;
        Display(--iNo);
    }
    


}

int main()
{
    Display();
    return 0;
}