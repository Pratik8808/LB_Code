import java.io.*;
import java.security.MessageDigest;

public class Program446 {

    public static void main(String[] args) throws Exception {

        FileInputStream fis = new FileInputStream("data.txt");

        MessageDigest md = MessageDigest.getInstance("MD5");

        byte[] buffer = new byte[1024];
        int bytesRead;

        while ((bytesRead = fis.read(buffer)) != -1) {
            md.update(buffer, 0, bytesRead);
        }

        byte[] digest = md.digest();

        for (byte b : digest) {
            System.out.printf("%02x", b);
        }

        fis.close();
    }
}