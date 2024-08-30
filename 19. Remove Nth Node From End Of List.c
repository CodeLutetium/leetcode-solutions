/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode ListNode;

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // Edge case: only 1 item
    if (head->next == NULL) {
        return NULL;
    }

    ListNode* curr = head;
    ListNode* prev = NULL;
    ListNode* last_node = head;

    // Advance last_node by n steps
    for (int i = 1; i < n; i++) {
        last_node = last_node->next;
    }

    // Traverse to the end
    while (last_node->next) {
        last_node = last_node->next;
        prev = curr;
        curr = curr->next;
    }

    // Remove nth node from the last
    // Edge case: removing the head
    if (prev == NULL) {
        return curr->next;
    }
    prev->next = curr->next;
    return head;
}

/**
 * Time complexity: O(n) (one pass solution)
 * Space complexity: O(1)
 */