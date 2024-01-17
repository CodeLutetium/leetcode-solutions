# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max_diameter
        max_diameter = 0

        def depthOfSubTree(root):
            # Base case: null 
            if root is None:
                return -1

            # Calculate radius of left and right subtree
            global max_diameter
            left_diameter = depthOfSubTree(root.left)
            right_diameter = depthOfSubTree(root.right)

            # Update max_diameter
            max_diameter = max(max_diameter, left_diameter + right_diameter + 2)

            # Return current depth
            return max(left_diameter, right_diameter) + 1
        
        depthOfSubTree(root)
        return max_diameter

        
"""
Time complexity: O(n)
Space complexity: O(n)
"""