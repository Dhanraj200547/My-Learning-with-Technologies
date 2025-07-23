

public class reversearray {
    public static void main(String[] args) {
        int [] arr = { 1 ,2,3,4,5};
        reverse(arr, 0, arr.length - 1);
        for (int idx = 0; idx < arr.length; idx++) {
            System.out.print(arr[idx] + " ");
            
        }
    }
    static void reverse(int[] arr , int start , int end){
        while( start < end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
