public class reverseString {
    public static void main(String[] args) {
        System.out.println(isPrime( 8,7));
            }
            static String reverse(String s){
                if(s.isEmpty()){
                    return s;
                }
                return reverse(s.substring(1)) + s.charAt(0);
            }
            static boolean isPrime(int n , int i){
        if( i <= 1){
            return false;
        }
        if(i == 2){
            return true;
        }
        if( n % i == 0) return false;
        return isPrime(n, i - 1);
    }
}
