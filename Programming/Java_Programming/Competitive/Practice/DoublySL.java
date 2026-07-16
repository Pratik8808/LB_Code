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

class SLDoubly
{  private node first;

   private node last;
   private  int iCount;

   public void Display()
   {
      node temp=first;
      do{
        System.out.print("|"+temp.data+"|<->");
        temp=temp.next;

      }while(temp!=last.next);

   }
   public int Count()
   {
    return this.iCount;

   }

   public void InsertFirst(int iNo)
   {
        node newn=null;
        newn=new node(iNo);
      if(first==null && last ==null)
      {
         first=newn;
        
         
      }
      else 
      {
        newn.next=first;
        newn.prev=null;
        first=newn;
         
      }
      iCount++;
   }
   public void InsertAtLast(int iNo)
   {
     node newn=new node(iNo);
     node temp=first;

     if(first==null && last ==null)
      {
         first=newn;
        
         
      }
      else 
      {
        while(temp.next!=null)
        {
            temp=temp.next;
        }
         temp.next=newn;
         newn.prev=temp;

      }
      iCount++;
     

   }
   public void InsertAtPos(int iNo,int iPos)
   {    node newn=new node(iNo);
        node temp=first;
        int i=0;
        if(first==null)
        {   
            first=newn;

        }
        else 
        {
            for(i=1;i<iPos;i++)
            {
                temp=temp.next;

            }
            newn.next=temp.next;
            newn.prev=temp;
            temp.next=newn;
        }

      
    
   }
    public void deleteFirst()
     {

    }

    public void DeleteLast()
    {

    }
    public  void DeleteAtPos()
    {

    }

}



public class DoublySL {

    public static void main(String[] args) {
        
    }

    
}
