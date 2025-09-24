/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if (head == NULL) return NULL;
    int count = 0;
    struct ListNode* temp = head;
    while (temp != NULL) {
        temp = temp->next;
        count++;
    }
    int pos = count - n + 1;
    if (pos < 1 || pos > count) {
        printf("Invalid position");
        return head;
    }
    if (pos == 1) {
        struct ListNode* temp1 = head;
        head = head->next;
        free(temp1);
        return head;
    }
    temp = head;
    struct ListNode* prevnode = NULL;
    for (int i = 1; i < pos; i++) {
        prevnode = temp;
        temp = temp->next;
    }
    if (temp != NULL) {
        prevnode->next = temp->next;
        free(temp);
    }

    return head;
}

