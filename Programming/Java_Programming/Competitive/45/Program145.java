
    import java.io.*;
    import java.util.Scanner;

    public class Program145
    {

        public static void Openfile(String name) throws IOException
        {
            FileInputStream fobj;

            fobj=new FileInputStream(name);
        
            System.out.println(fobj);

            
            
            fobj.close();

        
            
        }
        public static void main(String ...args)throws IOException
        {
                String input="";
                Scanner sc =new Scanner(System.in);

                System.out.println("Enter the File name");

                input=sc.nextLine();

                Openfile(input);

        }
    }