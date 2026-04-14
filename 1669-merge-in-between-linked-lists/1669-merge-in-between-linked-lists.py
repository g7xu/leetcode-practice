# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # find starting and ending

        cur = list1
        c = 0
        while cur:
            if c == a - 1:
                start = cur
            elif c == b + 1:
                end = cur
            
            cur = cur.next
            c += 1

        start.next = list2

        while list2.next is not None:
            list2 = list2.next

        list2.next = end

        return list1

            