/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode head = new ListNode();
        ListNode prev = head;

        // Iterate while both of them has node node
        while (l1 != null && l2 != null) {
            // Move carry over and reset carry
            int digit = carry;
            carry = 0;

            // Add values together and update carry if digit exceeds 10
            digit += l1.val;
            digit += l2.val;
            if (digit >= 10) {
                digit -= 10;
                carry = 1;
            }

            // Advance nodes
            l1 = l1.next;
            l2 = l2.next;

            // Update results ll
            ListNode digitNode = new ListNode(digit);
            prev.next = digitNode;
            prev = digitNode;

        }

        // Add remaining nodes to result
        while (l1 != null) {
            // Add digits
            int digit = carry;
            carry = 0;
            digit += l1.val;

            // Check for carry
            if (digit >= 10) {
                carry = 1;
                digit -= 10;
            }

            // Advance node
            l1 = l1.next;

            // Update results ll
            ListNode digitNode = new ListNode(digit);
            prev.next = digitNode;
            prev = digitNode;

        }

        // Add remaining nodes to result
        while (l2 != null) {
            // Add digits
            int digit = carry;
            carry = 0;
            digit += l2.val;

            // Check for carry
            if (digit >= 10) {
                carry = 1;
                digit -= 10;
            }

            // Advance node
            l2 = l2.next;

            // Update results ll
            ListNode digitNode = new ListNode(digit);
            prev.next = digitNode;
            prev = digitNode;

        }

        // Add carry 
        if (carry == 1) {
            prev.next = new ListNode(1);
        }

        return head.next;
    }
}