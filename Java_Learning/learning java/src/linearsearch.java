import java.util.Scanner;

public class linearsearch {
    public static void main(String[] args) {
        int[] arr = { 55,22,11,33,66,77};
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the target value :");
        int target = input.nextInt();
        for (int i = 0 ; i < arr.length ; i++){
            if(arr[i] == target){
                System.err.println("Target is found at index :"+ i);
                
            }
        }
    }
    
}
