class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2)
            return nums.length;

        int res = 1;
        int num_duplicates = 0;
        int j = 1;  // Used to keep track where to store the next number

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1] && ++num_duplicates < 2) {
                nums[j++] = nums[i];
                res++;
            } else if (nums[i] != nums[i-1]) {
                nums[j++] = nums[i];
                num_duplicates = 0;
                res++;
            }
        }
        
        return res;
    }
}