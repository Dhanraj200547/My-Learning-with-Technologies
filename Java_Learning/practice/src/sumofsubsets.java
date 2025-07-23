import java.util.ArrayList;
import java.util.List;

public class sumofsubsets {
    public static void main(String[] args) {
        int [] arr = { 1 , 2,3,4,5};
        int target = 6;
        findsubsets(arr, target, new ArrayList<>(), 0, 0);
    }
    static void findsubsets(int [] arr,int target ,List<Integer> subsets,int index ,int sum) {
        if( sum == target){
            System.out.println(subsets);
            return;
        }
        if(index >= arr.length || sum > target){
            return;
        }
        subsets.add(arr[index]);
        findsubsets(arr, target, subsets, index + 1, sum + arr[index]);
        subsets.remove(subsets.size() -1);
        findsubsets(arr, target, subsets, index + 1, sum);
    }
}
