class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num_chunks = time // (n-1)
        if num_chunks % 2 == 0:
            return time % (n - 1) + 1
        else:
            return n - time % (n - 1)
        
"""
Time complexity: O(1)
Space complexity: O(1)
"""