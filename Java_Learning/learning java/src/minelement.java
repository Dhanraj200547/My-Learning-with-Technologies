public class minelement {
    public static void main(String[] args) {
        int [] arr = { 56,25,98,14,12,0,21};
        int min = arr[0];
        for(int i= 0;i< arr.length;i++){
            if (arr[i] < min ){
                min = arr[i];
            }
        }System.out.println(min);
    }
    
}
