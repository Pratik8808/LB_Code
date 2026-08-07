
import java.io.*;
import java.util.Scanner;
class Program345
{
    public static void OpenFile(String FileName,String Data)
    {
        File fobj=new File(FileName);
        if(fobj.exists())
        {
            System.out.println("File Found Proccing for write operation");
        }
        else 
        {
            System.out.println("Unable to find the file in currrent directory");
            return;
        }
         FileOutputStream fd=null;
        try
        {
            fd=new FileOutputStream(FileName,true);
            fd.write(Data.getBytes());
            System.out.println("Data Sucessfully");
            fd.close();



        }
        catch(Exception e)
        {
            System.out.println(e);
        }
        
    }
    public static void main(String[] args) 
    {   
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter File Name");
        String input=sc.nextLine();
        System.out.println("Enter the Data");
        String Data=sc.nextLine();
        OpenFile(input, Data);

    }
}