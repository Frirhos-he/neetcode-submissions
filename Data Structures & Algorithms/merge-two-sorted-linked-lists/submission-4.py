# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        list1, list2 = (list1, list2) if list1.val <= list2.val else (list2, list1)

        head = list1
        prev = list1
        list1 = list1.next

        while list1 and list2:
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
