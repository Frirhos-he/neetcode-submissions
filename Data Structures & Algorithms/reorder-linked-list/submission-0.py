# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def number_of_elements(self, node: Optional[ListNode]) -> int:
        res = 0
        tmp = node
        while tmp != None:
            res+=1
            tmp = tmp.next
        return res

    def get_splitted_nth_nodes(self, node: Optional[ListNode], index : int):
        tmp = node
        curr_index = 1
        while curr_index < index:
            curr_index+=1
            tmp = tmp.next
        second = tmp.next
        tmp.next = None
        return node, second

    def reverseNodes(self, node: ListNode) -> ListNode:
        prev = None
        curr = node
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def mergeLists(self, head1, head2):
        dummy = head1

        while head1 and head2:
            tmp1 = head1.next
            tmp2 = head2.next

            head1.next = head2
            head2.next = tmp1

            head1 = tmp1
            head2 = tmp2

        return dummy

    def reorderList(self, head: Optional[ListNode]) -> None:
        n_elements = self.number_of_elements(head)
        if n_elements == 0:
            return
        half_element = n_elements // 2 + n_elements % 2
        head, half_head = self.get_splitted_nth_nodes(head, half_element)
        reversed_half_head = self.reverseNodes(half_head)
        self.mergeLists(head,reversed_half_head)
        