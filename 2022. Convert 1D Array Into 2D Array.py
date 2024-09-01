class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Case: no. of elements dont match
        if len(original) != (m * n):
            return []

        res =[[0] * n for _ in range(m)]
        idx = 0

        for row in range(m):
            for col in range(n):
                res[row][col] = original[idx]
                idx += 1
        return res
    
"""
Time complexity: O(n)
Space complexity: O(n)
"""