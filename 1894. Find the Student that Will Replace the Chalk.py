class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Reduce the number of loops
        k %= sum(chalk)
        used = 0
        student =  0

        while used + chalk[student % len(chalk)] <= k:
            used += chalk[student % len(chalk)]
            student += 1
        
        return student % len(chalk)
    
"""
Time complexity: O(n)
Space complexity: O(1)
"""