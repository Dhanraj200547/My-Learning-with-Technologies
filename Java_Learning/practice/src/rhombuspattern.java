public class rhombuspattern{
    public static void main(String[] args) {
        int n = 3;
        for(int i = 0 ; i < n ;i++){
            for(int j = 1 ; j <= 2 * n - 1 ;j++){
                if(j == n - i || j == n + i){
                    System.out.print("*");
                }else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        for(int i = n -1 ; i >= 0 ;i--){
            for(int j = 1 ; j <= 2 * n -1 ; j++ ){
                if(j == n - i || j == n + i){
                    System.out.print("*");
                }else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}