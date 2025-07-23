public class reccursion {
    public static void main(String[] args) {
        System.out.println(reversenum(123,0));
                   }
    @SuppressWarnings("unused")
                   static int  SumofDigits(int n){
                       if(n <= 0){
                           return 0;
                       }
                       return n % 10 + SumofDigits(n / 10);
                   }
                   @SuppressWarnings("unused")
                   static void print1ton(int n){
                       if( n == 0){
                           return;
                       }
                       System.out.println(n);
                       print1ton(n-1);
                       
                       
                   }
                   @SuppressWarnings("unused")
                    static int fact(int n){
                    if(n == 1){
                    return 1;
                    }
                    return n * fact(n-1);
                   }
                   @SuppressWarnings("unused")
                   static int sumofn(int n){
                    if( n == 1){
                        return 1;
                    }
                    return n + sumofn(n-1);
                   }
                   @SuppressWarnings("unused")
                   static int fiboancci(int n){
                    if( n == 0 || n ==1){
                        return n;
                    }
                    return fiboancci(n -1) + fiboancci(n -2);
                   }
                   @SuppressWarnings("unused")
                   static int power(int a , int b){
                    if( b == 0){
                        return 1;
                    }
                    return a * power( a , b -1);
                   }
                   @SuppressWarnings("unused")
                   static int countdigits(int n){
                    if( n == 0){
                        return 0;
                    }
                    return 1 + countdigits( n / 10);
                   }
                   @SuppressWarnings("unused")
                   static String reverseStr(String s){
            if( s.isEmpty()){
                return s;
            }
            return reverseStr(s.substring(1)) + s.charAt(0);
           }
           @SuppressWarnings("unused")
           static void printReverseArray(int[] arr, int n){
            if( n == 0){
                return;
            }
            System.out.print(arr[n -1] + " ");
            printReverseArray(arr, n -1);
           }
           @SuppressWarnings("unused")
           static int countzeroes(int n){
            if( n == 0){
                return 0;
            }
            if( n % 10 == 0){
             return 1 + countzeroes(n /10);
            }
            else{
                return countzeroes(n/10);
            }
           } 
           @SuppressWarnings("unused")
           static int maxElement(int[] arr ,int m , int n ){
            if(n ==0){
                return m;
            }
                if(m < arr[n]){
                    m = arr[n];
                }
                  return  maxElement(arr, m, n -1);
                
           }
           static int search(int[] arr , int n,int target){
            if(n == 0){
                return 0;
            }
            else if(arr[n] == target){ 
                return n;
            }
            return search(arr, n - 1, target);
           }

           static int binarySearch(int[] arr,int start ,int end, int target){
            if( start > end){
                return -1;
            }
            int mid = start + end /2;
            
            if(arr[mid] == target){
                return mid;
            }
            else if( target > arr[mid]){
                return binarySearch(arr,  mid + 1, end, target);
            }
            else if(target < arr[mid]){
                return binarySearch(arr, start, mid - 1, target);
            }
            return -1;
           }
           static void pattern1(int i,int j){
            if (i == 0) {
                return;
            }
            if (j < i) {
                pattern1(i, j + 1);
                System.out.print("* ");
                
            }
            if (i == j) {
                pattern1(i - 1, 0);
                System.out.println();
            }
           }
           static void pattern2(int i , int j , int space){
            if( i == 0){
                return;
            }
            if( space > i){
                pattern2(i, j ,space - 1);
                System.out.print(" ");
                
            }else if( j < i ){
                pattern2(i, j + 1, space);
                System.out.print("* ");
                
            }
            else {
                pattern2(i -1, 0 ,5);
                System.out.println();
                
            }
           }
           static int reversenum(int n,int digits){
              if( n == 0){
                return digits;
                
              }
              return reversenum(n/10 , (digits*10) + n % 10);
          }

}
