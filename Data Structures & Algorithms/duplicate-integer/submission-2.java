class Solution {
    public boolean hasDuplicate(int[] nums) {


        HashSet hs = new HashSet();

        if (nums.length == 0){
            return false;
        }

        for(int num : nums){
            hs.add(num);

        }
        return  hs.size() !=  nums.length ? true : false ;
    }

}