# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k

        # Get overall length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Get number of elements per part
        num_list = [0] * k
        if length < k:
            for i in range(length):
                num_list[i] = 1
        else:
            for i in range(k):
                num_list[i] = length // k
            remainder = length % k
            for i in range(remainder):
                num_list[i] += 1

        # Add linked list into res
        curr = head
        for i in range(k):
            # Add head to list
            res[i] = curr

            # Traverse to last node
            for j in range(num_list[i] - 1):
                curr = curr.next

            # Early return if last node
            if not curr:
                return res

            next_node = curr.next
            curr.next = None
            curr = next_node

        return res

"""
Time complexity: O(n)
Space complexity: O(1)
"""