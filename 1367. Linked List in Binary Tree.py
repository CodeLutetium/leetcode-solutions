# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Solution 1: DFS + Recursion

Time complexity: O(n * m) where n is the number of nodes in the linked list and m is the number of nodes in the binary tree.
"""
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Search for path from current root
        def dfs(head, root):
            # Reached end of list
            if not head:
                return True

            # Reached end of tree
            if not root:
                return False

            # Value matches
            if head.val == root.val:
                return dfs(head.next, root.left) or dfs(head.next, root.right)

            # Value does not match: early return
            return False

        # Reached end
        if not root: 
            return False

        # Current root is a start of path OR one of the child is the start of path
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

