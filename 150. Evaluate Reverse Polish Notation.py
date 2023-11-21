class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            # If number, push into stack
            if token.lstrip("-").isdigit():
                stack.append(token)
            # Else if operator, pop 2 items from stack and evaluate
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                else:
                    res = int(float(num1) / num2)
                stack.append(res)
        
        return int(stack[0])

"""
Time complexity: O(n)
Space complexity: O(n)
"""