import java.util.Scanner;
import java.io.*;
public class Program547 
{
    public static void LogFileUp(String Directory)
    {
        File s1=new File(Directory);


        if(s1.isDirectory())
        {   try
            {
                BufferedWriter s2=new BufferedWriter(new FileWriter("Marvellous.txt",true));
                File[] file=s1.listFiles();
                            for(File f:file)
                            {
                                String s="File Name is \t:"+f.getName().toString()+"\t \t Size of File is :"+f.length();
                                s2.write(s);
                                s2.newLine();
                            }
                    s2.close();
                    System.out.println("Sucessfully Copied all Data\n");

            }
            catch(Exception e)
            {
                System.out.println(e);
            }
          

        }
    }
  public static void main(String A[])
  {
     Scanner sc = new Scanner(System.in);

        System.out.println("Enter Directory Name:");
        String s1 = sc.nextLine();

        LogFileUp(s1);
  }       
}
