public class mininrotatedsortedarray {
    public static void main(String[] args) {
        int[] nums = { 3,4,5,1,2};
        int k = 0;
        for(int i = 0 ; i <nums.length  ; i++){
            if(nums[i] > nums[i+1]){
                k += 1;
            }else{
                break;
            }
        }
        while( k >0){
            int temp = nums[0];
            for(int i = 1 ; i < nums.length ;i++){
            nums[i-1] = nums[i];
            }
            nums[nums.length-1] = temp;
            k--;
        }
    System.out.println(nums[0]);
    }
}
