
class node 
{
    int data;
    node next;
    node prev;
    node (int iNo)
    {
        this.data=iNo;
        this.next=null;
        this.prev=null;
    }

}

class CLDoubly
{ 
     private node first;
     private node last;


   private  int iCount;

   public void Display()
   {
      node temp=first;
      do
      {
        System.out.print("|"+temp.data+"|<->");
        temp=temp.next;

      }while(temp!=last.next);
      System.out.println(" ");
   }
   public int Count()
   {
    return this.iCount;

   }

   public void InsertFirst(int iNo)
   {
        node newn=null;
        newn=new node(iNo);
      if(first==null)
      {
         first=newn;
         last=newn;
        
      }
      else 
      {
        newn.next=first;
        newn.prev=null;
        first.prev=newn;
        first=newn;
        
         
      }
      iCount++;
      first.prev=last;
      last.next=first;
   }

   public void InsertLast(int iNo)
   { 
       node newn=null;
        newn=new node(iNo);
      if(first==null)
      {
         first=newn;
         last=newn;
        
      }
      else 
      {
       last.next=newn;
       newn.prev=last;
       last=newn;
         
      }
      iCount++;
      first.prev=last;
      last.next=first;
   }

   public void InserAtPos(int iNo,int iPos)
   {
     node newn=new node(iNo);
     int i=0;

    if (iPos<1 ||iPos>iCount+1)
    {
         System.out.println("Invaild Position");
         return;
    }
    if(iPos==1)
    {
        InsertFirst(iNo);

    }
    if (iPos==iCount+1)
    {
        InsertLast(iNo);
    }
  

    else
    {
        node temp=first;
        for(i=1;i<iPos-1;i++)
        {
            temp=temp.next;
        }
        newn.next=temp.next;
        newn.prev=temp;
        temp.next=newn;
        
        iCount++;
    }
   }

   public void deleteFirst()
   {
      if(first==null)
      {
        return;
      }
      else if(first.next==last)
      {
        first=null;
        last=null;
      }
      else 
      {
         first=first.next;
        

      }
       first.prev=last;
       last.next=first;
      iCount--;
   }

   public void deleteLast()
   {
      
       if(first==null && last==null)
       {
          return;
       }
       else if(first.next==last)
       {
           first=null;

           last=null;
       }
       else
       {
        last=last.prev;
        last.next=first;
       }
       iCount--;

      
   }

   public void DeleteAtPos(int iPost)
   {
    
     int i=0;
     if(iPost<1 || iPost>iCount)

        {
            System.out.println("Invaild position");
            return;
        }
    if(iPost==1)
    {
        deleteFirst();
    }
    else if(iPost==iCount)
    {
        deleteLast();
    }
    else 
    {
      node temp=first;
      for(i=1;i<iPost-1;i++)
      {
          temp=temp.next;
      }
       temp.next=temp.next.next;
       temp.next.next.prev=temp;
    


    }
    iCount--;
   }

}



public class DoublyCL {
  
   public static void main(String []A)
   {
      CLDoubly sobj=new CLDoubly();
      sobj.InsertFirst(51);
      sobj.InsertFirst(21);
      sobj.InsertFirst(11);
      sobj.InsertLast(101);
      sobj.InsertLast(121);

      sobj.Display();
      System.out.println("Count Of Node is"+sobj.Count());

      sobj.InserAtPos(105, 4);


      sobj.Display();
      System.out.println("Count Of Node is"+sobj.Count());

      sobj.deleteLast();
      sobj.deleteFirst();

      sobj.Display();
      System.out.println("Count Of Node is"+sobj.Count());

      sobj.DeleteAtPos( 3);

       sobj.Display();
       System.out.println("Count Of Node is"+sobj.Count());








   }

    
}
