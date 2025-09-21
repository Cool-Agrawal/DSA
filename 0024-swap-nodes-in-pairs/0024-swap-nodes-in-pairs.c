/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* dummy =(struct ListNode *)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode* temp = dummy;
    struct ListNode* temp1 = temp->next;

    while(temp1 != NULL && temp1 ->next != NULL){
        temp->next = temp1->next;
        temp1->next = temp->next->next;
        temp->next->next = temp1;
        temp = temp1;
        temp1 = temp1->next;
    }
    return dummy->next;
}