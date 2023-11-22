class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        """
        Solution is from Neetcode.

        - Only add open parentheses if open < n
        - Only add closed parentheses if closed < open
        - Valid IFF open == closed == n
        """

        # Stack to hold parentheses
        stack = []

        # Hold results
        res = []

        # Recursive backtrack function
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # Pop character after backtrack returns

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res

