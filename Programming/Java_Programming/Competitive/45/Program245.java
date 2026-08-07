
    import java.io.*;
    import java.util.Scanner;

    public class Program245
    {

        public static void Openfile(String name) 
        {
            FileInputStream fobj=null;
            int iRet=0;
            try{
                fobj=new FileInputStream(name);

                // System.out.println(fobj);
                while(iRet!=-1)
                {
                    iRet=fobj.read();
                    System.out.print((char)iRet);
                }
            }
        
            catch(Exception IOException)
            {
                System.out.println(IOException);
            }
            finally
            {   
                if(fobj!=null)
                {
                    try{

                        fobj.close();
                    }
                    catch(Exception E)
                    {
                        System.out.println(E.getMessage());
                    }
                }
            }

            
            


        
            
        }
        public static void main(String ...args)
        {
                String input="";
                Scanner sc =new Scanner(System.in);

                System.out.println("Enter the File name");

                input=sc.nextLine();

                Openfile(input);

        }
    }