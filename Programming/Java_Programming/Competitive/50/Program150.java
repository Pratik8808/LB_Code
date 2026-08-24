        import java.util.Scanner;

        public class Program150 {
            public static int fareCalculation(int Distance,int surcharge)
            {
                if(Distance<0)
                {
                   return 0;
                }
                if(surcharge !=1 && surcharge!=0)
                {
                    System.out.println("Surcharge is not appiled as input is wrong");
                    return 0;
                }
                // Distance is Less than 10 kiloMeter  regular + base fare
                if(Distance<=10)
                {
                    if(surcharge==1)
                    {
                        int iTotal=(Distance*12+50)*120/100;
                    return iTotal;
                    }
                    else
                    {
                    return  Distance*12+50;
                    }
                
                }
            else
            {
                int beyond10=Distance-10;
                int totalBeyound10=beyond10*15;
                
                int itotal=(10*12)+totalBeyound10+50;
                if(surcharge==1)
                {
                    return itotal*120/100;
                }
                else
                {
                return itotal;
                }
                    

            }
            }


            public static void main(String[] A) 
            {
                Scanner Sc=new Scanner(System.in); 
                
                System.out.println("Enter total kilometers");
                int iNo=Sc.nextInt();

                System.out.println("is SurgeCharged Applied 1 for yes and 0 for no");
                int surcharge=Sc.nextInt();

                int TotalFare=fareCalculation(iNo,surcharge);

                System.out.println("Total Fares is :"+TotalFare);

                if(TotalFare!=0)
                {
                    System.out.println("Distance is :"+iNo);
                    if(surcharge==1)
                    {
                        System.out.println("Surge Charged Applied ");
                    }
                    else
                    {
                        System.out.println("SurgeCharge is not Applied");
                    }

                    System.out.println("Total fare is :"+TotalFare);
                }

                else
                {
                    System.out.println("Inavild input !!");
                }
            }
        }
