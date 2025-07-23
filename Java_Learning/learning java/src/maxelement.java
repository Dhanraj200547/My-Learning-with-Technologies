public class maxelement {
    public static void main(String args[]){
        int [] arr = { 22,15,6,18,586};
        int max = arr[0];
        for(int i = 0;i < arr.length ;i++){
            if(arr[i] > max){
                max = arr[i];
            }
        }System.out.println(max);
    }
    
}
