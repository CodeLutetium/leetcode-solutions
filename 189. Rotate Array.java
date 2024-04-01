class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        
        // Create left subarray from rotated (right) elements
        int[] leftArr = new int[k];
        int leftIndex = nums.length - k;
        for (int i = 0; i < k; i++) {
            leftArr[i] = nums[leftIndex++];
        }

        // Create right subarray from remaining (left) elements
        int[] rightArr = new int[nums.length - k];
        for (int i = 0; i < nums.length - k; i++) {
            rightArr[i] = nums[i];
        }

        // Merge two subarrays together
        for (int i = 0; i < k; i++) {
            nums[i] = leftArr[i];
        }
        int rightIdx = 0;
        for (int i = k; i < nums.length; i++) {
            nums[i] = rightArr[rightIdx++];
        }
    }
}

/*
 * Time complexity: O(n)
 * Space complexity: O(n)
 * 
 * Solution is not optimized
 */