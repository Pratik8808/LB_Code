#include <stdio.h>
#include <stdlib.h>

struct node 
{
    int data;
    struct node * next;
    struct node * prev;
};
typedef struct node NODE;
typedef struct node * PNODE;
typedef struct node ** PPNODE ;

void Display(PNODE first,PNODE last)
{
    do{
        printf("|%d|<->",first->data);
        first=first->next;

    }while(first!=last->next);
    printf("\n");
}

int Count(PNODE first,PNODE last)
{
    int iCount=0;
    do{
        first=first->next;
        iCount++;
        
    }while(first!=last->next);
    return iCount;
}

void Insertfirst(PPNODE first, PPNODE last,int iNo)
{
    PNODE newn=NULL;
    newn=(PNODE)malloc(sizeof(NODE));
    newn->data=iNo;
    newn->next=NULL;
    newn->prev=NULL;
    if(*first==NULL && *last==NULL )
    {
        *first=newn;
        *last=newn;
    }
    else 
    {
        newn->next=*first;
        (*first)->prev=newn;
        *first=newn;
    }
    (*first)->prev=*last;
    (*last)->next=*first;

}

void InsertAtLast(PPNODE first, PPNODE last, int iNO)
{
    PNODE newn=NULL;
    newn=(PNODE)malloc(sizeof(NODE));
    newn->data=iNO;
    newn->next=NULL;
    newn->prev=NULL;
    if(*first==NULL && *last==NULL )
    {
        *first=newn;
        *last=newn;
    }
    else 
    {
        (*last)->next=newn;
        newn->prev=*last;
        *last=newn;
        
    }
     (*first)->prev=*last;
    (*last)->next=*first;
}

void InsertAtPos(PPNODE first, PPNODE last, int iNo,int iPost)
{
    int i=0;
    PNODE temp=NULL;
    PNODE newn=NULL;
    newn=(PNODE)malloc(sizeof(NODE));
    newn->data=iNo;
    newn->next=NULL;
    newn->prev=NULL;
    int iCount=Count(*first,*last);

     if(*first==NULL && *last==NULL )
    {
        *first=newn;
        *last=newn;
    }
    if(iPost<1||iPost>iCount+1)
    {
        printf("Invaild Postion \n");
        return ;
    }
    if(iPost==1)
    {
        Insertfirst(first,last,iNo);


    }
    else if(iPost==iCount+1)
    {
        InsertAtLast(first ,last,iNo);
    }
    else 
    { temp=*first;
        for(i=1;i<iPost-1;i++)
        {
            temp=temp->next;

        }
         newn->next=temp->next;
         newn->prev=temp;
         temp->next->prev=newn;
         temp->next=newn;
       
    }
     (*first)->prev=*last;
    (*last)->next=*first;

    
}

void DeleteFirst(PPNODE first ,PPNODE last)
{
    if(*first==NULL && *last==NULL)
    {
        return;
    }
    else if((*first)->next==*last)
    {
        free(*first);
        free(*last);
        (*first)->next=NULL;
        (*last)->next=NULL;

    }
    else 
    {
        *first=(*first)->next;
        free((*first)->prev);


    }
    (*last)->next=*first;
    (*first)->prev=*last;
}

void DeleteAtlast(PPNODE first,PPNODE last)
{
    PNODE temp=NULL;
    temp=*first;
    if(*first==NULL && *last==NULL)
    {
        return;
    }
    else if((*first)->next==*last)
    {
        free(*first);
        free(*last);
        (*first)->next=NULL;
        (*last)->next=NULL;

    }
    else{
        
        
        while(temp->next!=(*last))
        {
            temp=temp->next;
        }
        free(temp->next);
        temp->next->prev=NULL;
        *last=temp;

    }
    (*last)->next=*first;
    (*first)->prev=*last;



}

void DeleteAtPos(PPNODE first, PPNODE last, int iPos)
{
     int i=0;
     PNODE temp=NULL;
    int iCount=Count(*first,*last);
    if(*first==NULL && *last==NULL)
    {
        return;
    }
    if( iPos<1|| iPos>iCount)
    {
        printf("Invaild Position");
        return;
    }
    if( iPos==1)
    {
        DeleteFirst(first,last);
    }
    else if(iPos==iCount)
    {
        DeleteAtlast(first,last);
    }
    else
    {
        temp=*first;
        for(i=1;i<iPos-1;i++)
        {
            temp=temp->next;
        }
        temp->next=temp->next->next;
        free(temp->next->prev);
        temp->next->prev=temp;



    }

}

int main()
{
    PNODE first=NULL;
    PNODE last=NULL;
    Insertfirst(&first,&last,101);
    Insertfirst(&first,&last,51);
    Insertfirst(&first,&last,21);
    Insertfirst(&first,&last,11);

    InsertAtLast(&first,&last,111);
    InsertAtLast(&first,&last,121);

    
    printf("Count of  Node is %d\n",Count(first,last));
    Display(first,last);

    InsertAtPos(&first,&last,105,3);

    printf("Count of  Node is %d\n",Count(first,last));
    Display(first,last);

    DeleteFirst(&first,&last);
    DeleteAtlast(&first,&last);
      printf("Count of  Node is %d\n",Count(first,last));
    Display(first,last);

    DeleteAtPos(&first,&last,3);

     printf("Count of  Node is %d\n",Count(first,last));
    Display(first,last);






    return 0;
}