public class cyclicsort {
    public static void main(String[] args) {
        int[] arr = { 5 , 4 ,3,2,1};
        sortcyclic(arr);
        for(int i = 0 ; i < arr.length ; i++){
            System.out.print(arr[i] + " ");
        }
    }
    static void sortcyclic(int[] arr){
        int i = 0 ;
        while (i < arr.length){
            int correct = arr[i] - 1;
            if(arr[i] !=arr[correct]){
                swap(arr, i , correct);
            }
            else{
                i++;
            }
        }
    }
    static void swap(int[] arr , int a ,int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}
