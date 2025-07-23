public class productarray {
        public static void main(String[] args) {
            int[] arr = { 11,22,33,44,55};
            int product = 1;
            for (int i = 0; i<arr.length ; i++){
                product = product * arr[i];
            } System.out.println(product);
        }
    
}
