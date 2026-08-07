
import java.util.Scanner;
import java.io.*;
public class Program246
{   public static void isFileExist(String FileName)
    {
        File s1=new File(FileName);
        if(s1.isFile())
        {
            System.out.println("File is Regular");
        }
        else
        {
            if(s1.exists())
            {

                System.out.println("File is not Regular File");
            }
            else
            {
                System.out.println("file is not Exist");
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter File name  to check File regular or not\n");
        String s1=sc.nextLine();
        isFileExist(s1);

    }
    
}