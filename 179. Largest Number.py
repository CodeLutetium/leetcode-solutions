class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert to string
        nums = [str(n) for n in nums]
        
        # Perform custom bubble sort
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                # Compare with number on the right
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                     nums[j], nums[i] = nums[i], nums[j]

        return "".join(nums).lstrip("0") or "0"

"""
Time complexity: O(n^2) due to bubble sort, can be optimized to O(nlogn) using other sorting methods
Space complexity: O(1)
"""