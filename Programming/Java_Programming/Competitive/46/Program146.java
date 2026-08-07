import java.util.Scanner;
import java.io.*;

public class Program146 {

    public static void copyData(String source ,String Dest)
    {
        File fobj1=new File(source);
        

        if(!fobj1.isFile())
        {
            System.out.println("Soure File cannot Opened has it not Exist as file");
        }
        try
        {
            BufferedReader fd1 = new BufferedReader(new FileReader(source));
            BufferedWriter fd2 =new BufferedWriter(new FileWriter(Dest,true));

            int iRet=0;
            while((iRet=fd1.read())!=-1)
            {   fd2.newLine();
                fd2.write(iRet);
               
            }
            fd1.close();
            fd2.close();
            System.out.println("Data copied Sucessfully");

        }
        catch(Exception e)
        {
            System.out.println("Unable to copy into File");
        }

    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Source File Name\n");
        String src=sc.nextLine();

        System.out.println("enter the Destionation file Name");
        String dest=sc.nextLine();

        copyData(src, dest);
        
        
    }
    
}
