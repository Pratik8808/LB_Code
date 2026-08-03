#include <stdio.h>
void Display(int iNo)
{
    
    if(iNo<=5)
    {
        
        Display(iNo+1);
        printf("%d\t",iNo);
    }
    


}

int main()
{
    Display(1);
    return 0;
}