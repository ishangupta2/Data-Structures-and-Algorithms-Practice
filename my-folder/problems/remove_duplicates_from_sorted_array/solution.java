class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 0;
        int index = 0;
        Set<Integer> set = new HashSet<>();
        for (int i =0; i < nums.length; i++) {
            if(!(set.contains(nums[i]))) {
                set.add(nums[i]);
                nums[index] = nums[i];
                index+=1;
                count+=1;
            } 
        }
        return count;
    }
}