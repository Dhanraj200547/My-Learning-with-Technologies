
import java.util.Scanner;

public class factorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        int a = 1;
        for (int i=1;i<=num;i++){
            
             a= a*i;
            
        }
        System.out.println(a);
    }
}
