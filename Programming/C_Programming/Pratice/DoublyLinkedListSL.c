# include <stdio.h>
# include <stdlib.h>

struct node
{
    int data;
    struct node * next;
    struct node *prev;


};
typedef struct node NODE;
typedef struct node * PNODE;
typedef struct node ** PPNODE;

void display(PNODE first)
{printf("\nNULL<=>");
    while(first!=NULL)
    {
        
        printf("|%d|->",first->data);
        first=first->next;
    }
    printf("NULL<=>\n");
}

int Count(PNODE first)
{
    int iCount=0;
    while(first!=NULL)
    {
        first=first->next;
        iCount++;
    }
    return iCount;
}

void InsertFirst(PPNODE first,int iNo )
{PNODE newn=NULL;
    newn=(PNODE)malloc(sizeof(NODE));
    newn->data=iNo;
    newn->next=NULL;
    newn->prev=NULL;


    if(*first ==NULL)
    {
        *first=newn;    
    }
    else
    {
        newn->next=(*first);
        (*first)->prev=(newn);
        (*first)=newn;
    }

  
}


  void InsertAtLast(PPNODE first ,int iNo)
    {   PNODE temp=NULL;
        PNODE newn=NULL;

        newn=(PNODE)malloc(sizeof(NODE));
        newn->data=iNo;
        newn->next=NULL;
        newn->prev=NULL;


      

        if(*first==NULL)
        {
           (*first)=newn;
        }
        
        else{
            temp=(*first);

            while(temp->next!=NULL)
            {
                temp=temp->next;
            }
            temp->next=newn;
            newn->prev=temp;
        }
        
    }


    void DeleteAtFirst(PPNODE first)
    {
        if(*first==NULL)
        {
            return;
        }
        else if((*first)->next ==NULL)
        {
            free((*first));
            (*first)->next=NULL;
        }
        else 
        {
           PNODE temp=(*first);
            (*first)=(*first)->next->next;
            free(temp);
            temp->next=NULL;
            (*first)->prev=NULL; //$
        }
    }

    void DeleteAtLast(PPNODE first)
    {
        PNODE temp=NULL;
         if(*first==NULL)
        {
            return;
        }
        else if((*first)->next ==NULL)
        {
            free((*first));
            (*first)->next=NULL;
        }
        else 
        {
            temp=*first;
            while(temp->next->next!=NULL)
            {
                temp=temp->next;

            }
            free(temp->next->next);
            temp->next=NULL;
        }
    }
    
    void InsertAtPost(PPNODE first,int iNo,int iPos)
    {
        int iCount=0;
        PNODE temp=NULL;
        iCount=Count(*first);

        if(iPos<0 || iPos>iCount+1)
        {
            printf("Invaild Postion");
            return;
        }
        else if(iPos==1)
        {
            InsertFirst(first,iNo);
        }
        else if(iPos==iCount+1)
        {
            InsertAtLast(first,iNo);
        }

    }

    void DeleteAtPost(PPNODE first, int iNo,int iPos)
    {
        int i=0;
        int iCount=Count((*first));
       if(first==NULL)
       {
        return;
       }
       if(iPos<1 || iPos>iCount)
       {
          printf("Wrong Postion\n");
          return;
       }
       if(iPos==1)
       {
        InsertFirst(first,iNo);
       }
       else if(iPos==iCount+1)
       {
        InsertAtLast(first,iNo);
       }
       else 
       {
          PNODE temp=*first;
         for (i=1;i<iPos-1;i++)
         {
            temp=temp->next;
         }
         temp->next=temp->next->next;
         free(temp->next->next->prev);
         temp->next->next->prev=temp;
          
       }

    }

int main()
{   int iRet=0;
    PNODE head=NULL;
    InsertAtLast(&head,11);
    InsertAtLast(&head,21);
    InsertAtLast(&head,51);
    InsertAtLast(&head,101);
      InsertAtLast(&head,111);
    iRet=Count(head);
    display(head);
    printf("Count after InsertAtLAst is %d\n",iRet);


    InsertFirst(&head,1);
     iRet=Count(head);
    display(head);
    printf("Count after InsertAtlast is %d\n",iRet);

    InsertAtPost(&head,105,3);
     iRet=Count(head);
    display(head);
    printf("Count after DeleteAtFirst is %d\n",iRet);




   

    
    return 0;

}