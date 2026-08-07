
import java.util.Scanner;
import java.io.*;
public class Program546
{   public static void ShowFileName(String FileName)
    {
        File s1=new File(FileName);
       if(s1.isDirectory())
       {
         File[] file=s1.listFiles();
         for(File f:file)
         {
            System.out.print(f.getName());
            System.out.print("\t \t "+f.length()+"in bytes"+"& Last Modfied on"+f.lastModified());
            System.out.println("");

         }
       }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter File name  to check File regular or not\n");
        String s1=sc.nextLine();
        ShowFileName(s1);

    }
    
}