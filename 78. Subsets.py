class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            # Reach full set
            if i >= len(nums):
                result.append(subset.copy())
                return
        
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # Decision to NOT include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return result  
    
"""
SOLUTION FROM NEETCODE
Time complexity: O(n * 2^n)
Space complexity: O(2^n)
"""