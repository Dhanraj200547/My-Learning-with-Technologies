public class newpattern {
    public static void main(String[] args) {
        pattern2(5,0,5);
    }
    static void pattern2(int i , int j , int space){
        if( i == 0){
            return;
        }
        if( j < i ){
            pattern2(i, j + 1, space);
            System.out.print("*");
        }
        else if( space > i){
            pattern2(i, j ,space - 1);
            System.out.print(" ");
        }
        else {
            pattern2(i -1, 0 ,5);
            System.out.println();
        }
       }
}
