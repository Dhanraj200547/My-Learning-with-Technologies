import java.util.Scanner;

public class loopsumandproduct {
    public static void main(String[] args) {
        int[] arr = {56,25,98,14,12,0,21 };
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the value of index a :");
        System.out.println("Enter the value of index b :");
        int a = input.nextInt();
        int b = input.nextInt();
        int sum = 0;
        int product = 1;
        for( int i = a;i <= b ; i++){
            sum = arr[i] + sum;
            product = arr[i]*product;

        }
        System.err.println("Sum of the value of indexes"+ a +" and "+ b+" are : "+ sum);
        System.err.println("Product of the value of indexes"+ a +" and "+ b+" are : "+ product);

    }
}
