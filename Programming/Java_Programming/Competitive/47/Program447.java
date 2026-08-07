import java.util.Scanner;
import java.io.*;

public class Program447
{
    public static void ShowFileName(String Directory)
    {
        File s1 = new File(Directory);
        String FileName = "Marvellous.txt";

        if(s1.isDirectory())
        {
            try
            {
                File[] files = s1.listFiles();

                BufferedWriter s2 = new BufferedWriter(new FileWriter(FileName, true));

                for(File f : files)
                {
                    if(f.isFile())
                    {
                        BufferedReader br=new BufferedReader(new FileReader(f));

                        int iRet=0;
                        while((iRet=br.read())!=-1)
                        {
                            s2.write(iRet);
                        }
                        s2.newLine();
                        

                        // System.out.println(f.getName());
                    }
                }

                s2.close();
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Directory Name:");
        String s1 = sc.nextLine();

        ShowFileName(s1);
    }
}