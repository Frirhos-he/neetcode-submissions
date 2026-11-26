# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr: ListNode | None = head
        succ: ListNode | None = head.next
        prec: ListNode | None = None
        while succ != None:
            curr.next = prec
            prec = curr

            tmp = succ.next
            succ.next = curr

            curr = succ
            
            succ = tmp
        return curr