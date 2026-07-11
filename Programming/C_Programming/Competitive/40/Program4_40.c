#include <stdio.h>

#include <stdlib.h>
#define True 0
#define False 1
typedef  int BOOL;

// InsetAtFirst 
struct node {
    int data;
    struct node * next;
};
typedef struct node NODE;
typedef struct node * PNODE;
typedef struct node ** PPNODE;

void Display(PNODE first)
{
      while(first!=NULL)
    {
        printf("|%d|->",first->data);
        first=first->next;
    }
    printf("NULL \n");
   
}
int count (PNODE first)
{
  return 0;
}

void InsertFirst(PPNODE first,int iNo)
{
    PNODE newn=NULL;
    newn=(PNODE)malloc(sizeof(NODE));

    newn->data=iNo;
    newn->next=NULL;

    if(*first==NULL)// LinkedList is Empty
    {
        *first=newn;

    }
    else// LinkedList contain At least one Node 
    {
           newn->next=*first;
           *first=newn;
    }

    

}
void InsertLast(PPNODE first,int iNo)
{

    PNODE newn=NULL;
    newn=(PNODE)malloc(sizeof(NODE));

    newn->data=iNo;
   

    if(*first==NULL)// LinkedList is Empty
    {
        *first=newn;

    }
    else// LinkedList contain At least one Node 
    {
        PNODE temp=*first;

    }
}

int CountFrequency(PNODE first,int iNo)
{
    int iCount=0;

    while(first!=NULL)
    {
        if((first->data)==iNo)
        {
            iCount++;
        }
        first=first->next;
    }
    return iCount;
}





int main()
{
    PNODE head=NULL;
    int iRet=0;
    InsertFirst(&head,101);
    InsertFirst(&head,51);
    InsertFirst(&head,22);
    InsertFirst(&head,11);
    InsertFirst(&head,21);
    InsertFirst(&head,21);
    Display(head);
    iRet=CountFrequency(head,21);
    printf("Number of Frequency  in Nodes are %d\n",iRet);



   


       

    return 0;
}