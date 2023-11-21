class MinStack(object):

    def __init__(self):
        # min_stack is auxillary stack to help us keep track of min element
        self.min_stack = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """,
        # If value is smaller than topmost element of min stack, add it in
        if self.min_stack == [] or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        n = self.stack.pop()
        # Remove from min_stack if it is min, to update current min
        if self.min_stack[-1] == n:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Time complexity: O(1) for each function
Space complexity: O(2n) = O(n) (use of auxillary stack)
"""