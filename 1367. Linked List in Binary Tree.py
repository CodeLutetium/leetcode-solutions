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
Space complexty: O(n + m)
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

"""
Solution 2: Iterative (similar to recursive DFS)

Time complexity: O(n * m)
Space complexity: O(n) due to stack
"""
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Search for path starting from tree_node
        def isMatch(node, head) -> bool:
            if not node:
                return False

            stack = []
            stack.append((node, head))

            while stack:
                curr_node, curr_list = stack.pop()

                # Reached end of list
                if curr_list == None:
                    return True

                if not curr_node:
                    continue

                if curr_node.val == curr_list.val:
                    stack.append((curr_node.left, curr_list.next))
                    stack.append((curr_node.right, curr_list.next))

            return False

        if not root:
            return False
        
        nodes = []
        nodes.append(root)

        while nodes:
            tree_node = nodes.pop()

            if isMatch(tree_node, head):
                return True
            
            if tree_node:
                nodes.append(tree_node.left)
                nodes.append(tree_node.right)

        return False
            