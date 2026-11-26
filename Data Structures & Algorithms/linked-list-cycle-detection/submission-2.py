# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = rabbit = head

        while rabbit != None and rabbit.next != None and rabbit.next.next != None:
            rabbit = rabbit.next.next
            if rabbit == turtle:
                return True
            turtle = turtle.next
        return False
        