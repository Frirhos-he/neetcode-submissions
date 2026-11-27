# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def n_elements(self, node: ListNode):
        tmp = node
        elements = 0
        while tmp != None:
            elements += 1
            tmp = tmp.next
        return elements

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        index = 0
        prev = head
        n_elements = self.n_elements(head)

        designed_index = n_elements - n
        if designed_index == 0:
            return head.next
        while index < designed_index - 1:
            prev = prev.next
            index+=1
        succ = prev.next.next if prev.next else None
        prev.next = succ
        return head
