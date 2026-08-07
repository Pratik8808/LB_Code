
import java.util.Scanner;
import java.io.*;
public class Program147 
{   public static void ShowFileName(String Directory)
    {
        File s1=new File(Directory);
        if(s1.isDirectory())
        {
            File [] file=s1.listFiles();
            for(File f:file)
            {
                if(f.isFile())
                {
                    System.out.println(f.getName());
                }
            }
        }
    }
    public static void main(String[] args) 
    {   Scanner sc=new Scanner(System.in);
      
        System.out.println("Enter File name  to check File regular or not\n");
        String s1=sc.nextLine();
        ShowFileName(s1);


    }    
}
