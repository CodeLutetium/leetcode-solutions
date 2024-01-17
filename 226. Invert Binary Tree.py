# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Empty tree
        if root == None:
            return

        # Base case: Leaf node
        if root.left == None and root.right == None: 
            return root
        # Swap child nodes
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

            
"""
Time complexity: O(n)
Space complexity: O(n)
"""