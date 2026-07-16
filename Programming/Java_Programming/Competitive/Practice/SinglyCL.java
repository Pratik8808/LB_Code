class node
{
   public int data;
   public  node next;

   node(int iNo)
   {
    this.data=iNo;
    this.next=null;
   }
}

class Singlycl
{   
    private node first;
    private node last;
    private int iCount;
    
    void Display()
    {
        node temp=first;
    do{
        System.out.print("|"+temp.data+"|->");
        temp=temp.next;
    }while(temp!=last.next);
        System.out.println();
    }
    int Count()
    {
        return this.iCount;
    }

    void InsertAtFirst(int iNo)
    {
        node newn=null;
        newn=new node(iNo);

        if(first==null && last==null)
        {
            first=newn;
            last=newn;

        }
        else 
        {
            newn.next=first;
            first=newn;
            
        }
        last.next=first;

        iCount++;

    }

    void InsertAtLast(int iNo)
    {
            node newn=null; // reference
            newn=new node(iNo);
          if(first==null)
        {
            first=newn;
            last=newn;

        }
        else 
        {
            last.next=newn;
            newn.next=first;
            last=newn;
            
        }
        iCount++;
    }

    void InsertAtpos(int iNo,int iPos)
    {
        node newn=null;
        newn=new node(iNo);
        int i=0;
        if(iPos<1||iPos>iCount+1)
        {
            System.out.println("INvaild Statment");
            return;
        }
        if(iPos==1)
        {
            InsertAtFirst(iNo);

        }
        else if(iPos==iCount+1)
        {
            InsertAtLast(iNo);
        }
        else 
        {
           node temp=first;
           for (i=1;i<iPos-1;i++)
           {
            temp=temp.next;
           }
           newn.next=temp.next;
           temp.next=newn;
        }


    }

  public void  Deletefirst()
    {
        if(first ==null && last==null)
        {
            return;
        }
       else if(first==last)
        {   first=null;
            last=null;
        }
        else 
        {
            first=first.next;
            last.next=first;
        }
        iCount--;

    }
 public void DeleteLast()
 {
    if(first ==null && last==null)
        {
            return;
        }
       else if(first==last)
        {   first=null;
            last=null;
        }
        else 
        {
           node temp=null;
           temp=first;
           while(temp.next!=last)
           {
            temp=temp.next;
           }
           temp.next=null;
           last=temp;
           last.next=first;

        }
        iCount--;
 }

 public  void deleteAtPos(int iPos)
 {
    int i=0;
    if(iPos<1|| iPos>iCount)
    {
        System.out.println("Invaild Postion");
        return;
    }
    if(iPos==1)
    {
        Deletefirst();
    }
    else if(iPos==iCount)
    {
        DeleteLast();
    }
    else 
    {
        node temp=first;
        for(i=1;i<iPos-1;i++)
        {
            temp=temp.next;
        }
        temp.next=temp.next.next;
        iCount--;
    }
 }


}

class SinglyCL
{
    public static void main(String A[])
    {
        Singlycl sobj =new Singlycl();

        sobj.InsertAtFirst(51);
        sobj.InsertAtFirst(21);
        sobj.InsertAtFirst(11);
        sobj.InsertAtLast(101);
        sobj.InsertAtLast(121);

        sobj.Display();
        System.out.println(sobj.Count());
        sobj.InsertAtLast(151);
        sobj.Display();
        System.out.println(sobj.Count());

        sobj.DeleteLast();
        sobj.Deletefirst();
         sobj.Display();
        System.out.println(sobj.Count());
        sobj.deleteAtPos(3);
        sobj.Display();
        System.out.println(sobj.Count());

     

       
        


    }

}