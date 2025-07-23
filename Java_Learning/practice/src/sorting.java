
class sorting{
    public static void main(String args[]){
        int[] arr = { 5 , 4 ,3,2,1};
        insertionSort(arr);
        for(int i = 0 ; i < arr.length ; i++){
            System.out.print(arr[i] + " ");
        }

    }
    static void bubblesort(int[] arr , int n ){
        boolean swapped ;
        for(int i = 0 ; i < n - 1 ; i++){
            swapped = false;
            for(int j = 0 ; j <n - i -  1 ;j++){
                if(arr[j] > arr[j + 1] ){
                    swap(arr , j , j + 1);
                    swapped = true;
                }
            }
            if(swapped == false){
                break;
            }
        }
    }
    static void selection(int[] arr , int n){
        int index = arr.length - 1;
        for(int i = 0; i < n; i++){
            int a = max(arr, n-i);
            swap(arr, a , index);
            index--;
        }
    }
    static int max(int [] arr , int n){
        int max = 0;
        for(int i = 0 ; i < n  ; i++){
            if(arr[i] > arr[max]){
                max = i;
            }
        }
        return max;
    }
    static void swap(int[] arr ,int a , int b){
        int temp;
        temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    static void insertionSort(int[] arr){
        for(int i = 0 ; i < arr.length - 1 ; i++){
            for(int j = i + 1 ; j > 0 ; j--){
                if(arr[j - 1] > arr[j]){
                    swap(arr , j-1 , j);
                }else{
                    break;
                }
            }
        }
    }
}