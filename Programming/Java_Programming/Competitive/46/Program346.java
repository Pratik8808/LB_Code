
import java.io.*;
import java.util.Scanner;
public class Program346 {
    public static void isDirectory(String s1)
    {   
        File s2=new File(s1);
        if(s2.isDirectory())
        {
            System.out.println("Directory already Present");
        }
        else
        {
            s2.mkdir();
            System.out.println("Directory is Created Sucessfully");
        }

    }

    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Directory Name ");
        String input=sc.nextLine();
        isDirectory(input);
        
    }
}
