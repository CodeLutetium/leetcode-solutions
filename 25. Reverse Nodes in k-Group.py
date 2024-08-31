# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Returns tuple of first and last element in the reversed sub grp
    def reverseSubGroup(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        last_element = head

        while curr:
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev, last_element   # new_head, new_tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        curr = head
        new_head = head
        sub_head = head
        prev_tail = None

        while curr:
            counter += 1

            if counter % k == 0:
                # Unlink the last node
                next_node = curr.next
                curr.next = None

                # Reverse the current segment
                (sub_head, tail) = self.reverseSubGroup(sub_head)

                if prev_tail:
                    prev_tail.next = sub_head
                else:
                    new_head = sub_head

                prev_tail = tail
                tail.next = next_node
                sub_head = next_node
                curr = next_node
            else:
                curr = curr.next

        return new_head
        