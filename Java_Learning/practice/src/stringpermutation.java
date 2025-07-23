public class stringpermutation {
    public static void main(String[] args) {
        String str = "abcd";
        boolean[] used = new boolean[str.length()];
        subsets(str, "", used);
    }
    static void subsets(String str,String perms , boolean[] used){
        if(perms.length() == str.length()){
            System.out.println(perms);
            return;
        }
        for(int i= 0;i<str.length();i++){
            if(!used[i]){
                used[i] = true;
                subsets(str, perms + str.charAt(i), used);
                used[i] = false;
            }
        }
    }
}
