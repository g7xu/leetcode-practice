# loop through the linkedin list once
# using stack to store all the reference

# track the number
# while loop to insert, until reach the size number and stop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        pre = s.next = None
        while second:
            tmp = second.next
            second.next = pre
            pre = second
            second = tmp

        first, second = head, pre
        while second:
            # to_insert = second
            # second = second.next
            
            # tmp = first.next
            # first.next = to_insert
            # to_insert.next = tmp
            # first = tmp

            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head