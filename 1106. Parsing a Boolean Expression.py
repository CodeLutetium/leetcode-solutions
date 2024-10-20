class Solution:
    # Evaluate a list of values given an operator
    def evaluateSubExpr(self, operator, values) -> str:
        if operator == "!":
            return "f" if values[0] == "t" else "t"
        elif operator == "|":
            return "t" if "t" in values else "f"
        elif operator == "&":
            return "f" if "f" in values else "t"
          
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            # Push into stack if not closing bracket, else pop from stack and evaluate
            if char != ")":
                stack.append(char)
            else:
                # Closing bracket: Pop till matched opening bracket and evaluate subexpression
                values = []

                while stack[-1] != "(":
                    top = stack.pop()
                    if top == "f" or top == "t":
                        values.append(top)
                else:
                    # Remove "("
                    stack.pop()
                    operator = stack.pop() # Get the operator

                stack.append(self.evaluateSubExpr(operator, values))

        return True if stack[0] == "t" else False
