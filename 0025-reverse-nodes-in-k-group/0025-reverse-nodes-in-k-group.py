# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k== 1:
            return head
        curr = head
        c = 0
        while curr and c < k:
            curr = curr.next
            c += 1
        if c < k :
            return head
        prev = None
        curr = head
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = self.reverseKGroup(curr,k)
        return prev
    
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev