class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Index_1: i
        # Index_2: j
        i, j = 0, len(numbers) - 1

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else: 
                i += 1
        
        return [i+1, j+1] 
    
"""
Time complexity: O(n)
Space complexity: O(1)
"""