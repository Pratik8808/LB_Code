import java.util.Scanner;
import java.io.*;

public class Program445 {
    public static void OpenFile(String filename)
    {   
        File fobj=new File(filename);
        if(fobj.exists())
        {
            System.out.println("File is already Present in System");
        }
        else
        {   try
            {
                
               boolean s1= fobj.createNewFile();
               if(s1==true)
               {
                System.out.println("Created Suecessfully");
               }
               else
               {
                System.out.println("Unable to Create File ");
               }
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        }

    }
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter File Name");
        String input=sc.nextLine();
        System.out.println("Enter the Data");
        OpenFile(input);
    }
}
