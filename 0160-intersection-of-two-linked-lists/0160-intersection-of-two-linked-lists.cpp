/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *t1 = headA;
        ListNode *t2 = headB;
        int c1 = 0;
        int c2 = 0;
        while (t1 != NULL){
            c1 ++;
            t1 = t1->next;
        }
        while (t2 != NULL){
            c2 ++;
            t2 = t2->next;
        }

        int d = 0;
        ListNode *temp;
        ListNode *temp1;
        if (c1>c2){
            d = abs(c1-c2);
            temp = headA;
            temp1 = headB;
        }
        else{
            d = abs(c2-c1);
            temp = headB;
            temp1 = headA;
    }
    while (d>0){
        temp = temp->next;
        d --;
    }
    
    while (temp != NULL || temp1 != NULL){
        if (temp == temp1){
            return temp;
        }
        temp = temp->next;
        temp1 = temp1->next;
    }
    return NULL;
    }
};