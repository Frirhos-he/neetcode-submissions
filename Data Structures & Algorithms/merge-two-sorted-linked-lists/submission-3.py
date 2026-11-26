# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        list1, list2 = (list1, list2) if list1.val < list2.val else (list2, list1)
        head: ListNode | None = list1
        tmp = list1.next
        prev = list1
        list1 = tmp
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                prev.next = list2
                prev = list2
                list2 = list2.next
            else:
                prev.next = list1
                prev = list1 
                list1 = list1.next
        prev.next = list1 if list1 else list2

        return head
