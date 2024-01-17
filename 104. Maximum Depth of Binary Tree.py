# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepthHelper(self, root, depth):
        if root == None: 
            return 0

        # Leaf node 
        if root.left == None and root.right == None:
            return depth
        else:
            return max(self.maxDepthHelper(root.left, depth+1), self.maxDepthHelper(root.right, depth+1))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxDepthHelper(root, 1)
    

"""
Time complexity: O(n)
Space complexity: O(n) (assuming unbalanced binary tree)

Alternative solutions: 
1. BFS (O(n))
Use queue

2. Iterative DFS (O(n))
Use stack, add node AND depth to the stack
"""