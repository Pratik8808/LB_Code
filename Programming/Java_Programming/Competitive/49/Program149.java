
import java.util.Scanner;

class ParkingExpense
{
    private int iHours;
    private int iAmount;
    public ParkingExpense(int iHours,int iAmount)
    {
        this.iHours=iHours;
        this.iAmount=iAmount;
    }

    public int getiHours()
    {
        return iHours;
    }
    
    public int getiAmount()
    {
        return iAmount;
    }

}


public class Program149 
{
    public static ParkingExpense ParkingFees(int iHours)
    {
        ParkingExpense s1=null;
        if(iHours<= 2)
        {
            s1=new ParkingExpense(20,20);
            return s1;
        }
        else 
        {
          if(iHours>2 && iHours <=10)
          {
             int totalhours=iHours-2;
             int extra=totalhours*30;

             int total=extra+20;
            s1=new ParkingExpense(iHours, total);
            return s1;
          }

          else
          {
             int exceedhours=iHours-10;

             // Hours 2 to 10  price per hour is 30
             int firstPenalty=iHours-exceedhours-2;
             int totalFirstPenalty=firstPenalty*30;

             // After 10 hours

             int totalexceedPenalty=50+totalFirstPenalty+20;

             s1=new ParkingExpense(iHours, totalexceedPenalty);

             return s1;

          }
        }

    }
    public static void main(String[] A) {
        Scanner sobj=new Scanner(System.in);
        ParkingExpense s1=null;
        System.out.println("Enter total hours car parked");
        int ihours=sobj.nextInt();
        s1=ParkingFees(ihours);

        System.out.println("Total  Parking Duration :"+s1.getiHours());
        System.out.println("Total Parking fee is : "+s1.getiAmount());
        
    }    
}
