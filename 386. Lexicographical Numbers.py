class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1

        for i in range(n):
            res.append(curr)

            if curr * 10 <= n:
                curr *= 10
            else:
                # Multiplying curr by 10 will be more than n
                while curr % 10 == 9 or curr >= n:
                    # Remove the last digit
                    curr //= 10
                curr += 1
                
        return res
    
"""
Time complexity: O(n)
Space complexity: O(1)
"""