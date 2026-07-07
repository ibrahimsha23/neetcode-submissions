class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap <Integer, Integer> numCounter = new HashMap();



        for (int j=0; j< nums.length; j ++){
            int diff  = target - nums[j];

            if (numCounter.containsKey(diff)){
                return new int[]{numCounter.get(diff), j};
            }

            numCounter.put(nums[j], j);
        }
         return new int[]{};

    }
}
