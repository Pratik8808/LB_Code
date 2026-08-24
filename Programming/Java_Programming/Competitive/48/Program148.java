import java.util.Scanner;

public class Program148
{
  public int FineCalculator(int dayskept)
  {

        if(dayskept<=7)
        {
            return 0;
        }
        else
        {
            if(dayskept>7 &&  dayskept<=12)
            {
                int totalfineDays=dayskept-7;
                
                int fine=totalfineDays*5;   // fine Per Day till 7- 12 days

                return fine;
            }

            else 
            {
                int daysbeyound12=dayskept-12;
                
                int regularFine=5*5; // 8 to 12 days fine as 5 days fines

                int after12daysfine=daysbeyound12*10;  // fine after 12 days on 13 day each 10 so regularfine + after 13 days



                return after12daysfine+regularFine;
            }
        }


  }

    public static void main(String A[])
    {
        Scanner sc=new Scanner(System.in);

        System.out.println("Enter how many days Book kept");
        Program148 s1=new Program148();
        int iNo=sc.nextInt();

        int Result=s1.FineCalculator(iNo);

        if(Result==0)
        {
            System.out.println("No Fine");
        }
        else
        {
            System.out.println("Total fine is "+Result);
        }

    }
}