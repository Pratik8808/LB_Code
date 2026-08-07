import java.util.Scanner;
import java.io.*;
public class Program545 {
    public static void isDirectory(String Filename)
    {
        File fobj=new File(Filename);
        boolean s1= fobj.isDirectory();
        if(s1==true)
        {
            System.out.println("Directory is PResent ");
        }
        else
        {
            System.out.println("Driectory is not Present");
        }

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter File Name");
        String input=sc.nextLine();
     
        isDirectory(input);

    }
}
