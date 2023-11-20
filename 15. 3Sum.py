class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort() # O(nlogn)

        # Loop through index and each number of input array
        for i, a in enumerate(nums):
            # Skip if we are using the same value as prev
            if i > 0 and a == nums[i-1]:
                continue 
            
            # Two pointer solution (two sum on sorted array)
            l, r = i+1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
                
"""
Time complexity: O(nlogn) + O(n^2) = O(n^2)
Space compelxity: O(n) (for sorting)

Solution from neetcode
"""