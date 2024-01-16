/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* curr = head;
    struct ListNode* next = NULL;
    struct ListNode* prev = NULL;

// While current node is not null, move pointer forward
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

// Time complexity: O(n)
// Space complexity: O(1)