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

BOOL SerachElement(PNODE first,int iNO)
{
    BOOL flag=False;
    while(first!=NULL)
    {
        if(first->data==iNO)
        {
            flag=True;
            break;
        }
        first=first->next;

    }
    return flag;
}





int main()
{
    PNODE head=NULL;
    BOOL BRet=False;
    InsertFirst(&head,101);
    InsertFirst(&head,51);
    InsertFirst(&head,21);
    InsertFirst(&head,11);
    Display(head);
    int Value=0;
    printf("Enter the elemeent to serach in node \n");
    scanf("%d",&Value);
    BRet=SerachElement(head,Value);
    if(BRet==True)
    {
        printf("Elemet is present in Node\n");
    }
    else 
    {
        printf("Element is not Present in LinkedList\n");
    }


       

    return 0;
}