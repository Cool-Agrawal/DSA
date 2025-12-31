/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    if(head->next==NULL || head == NULL){
        return true;
    }
  
    if(head->next->next==NULL){
        if(head->val==head->next->val){
            return true;
        }
        else{
            return false;
        }
    }
    if(head->next->next->next==NULL){
        if(head->val==head->next->next->val){
            return true;
        }
        else{
            return false;
        }
    }

    struct ListNode *slow = head;
    struct ListNode *fast = head;
    while(fast != NULL && fast->next!=NULL){
    slow = slow->next;
    fast = fast->next->next;
    }
    struct ListNode *prevnode=NULL;
    struct ListNode *currnode,*nextnode;
      currnode=nextnode=slow;
      while(nextnode!=NULL){
        nextnode = nextnode->next;
        currnode->next = prevnode;
        prevnode = currnode;
        currnode = nextnode; 
      }
      slow=prevnode;
    fast = head;
    while(slow!= NULL){
        if(slow->val != fast->val){
                return false;
        }
        slow = slow ->next;
        fast = fast->next;
    }

    return true;
}