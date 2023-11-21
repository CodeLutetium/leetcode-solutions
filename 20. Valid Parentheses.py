class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for bracket in s:
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
            else:
                # Case 0: Empty stack
                if stack == []:
                    return
                open_bracket = stack.pop()

                # Case 1
                if open_bracket == "(" and bracket != ")":
                    return False 
                # Case 2
                elif open_bracket == "[" and bracket != "]":
                    return False
                # Case 3
                elif open_bracket == "{" and bracket != "}":
                    return False
        return stack == []
    

"""
Time complexity: O(n)
Space complexity: O(n)
"""