# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()


        p1 = list1
        p2 = list2
        cur = res
        while p1 or p2:
            if not p1:
                cur.next = ListNode(p2.val)
                cur = cur.next
                p2 = p2.next
            elif not p2:
                cur.next = ListNode(p1.val)
                cur = cur.next
                p1 = p1.next
            elif p1.val <= p2.val:
                cur.next = ListNode(p1.val)
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = ListNode(p2.val)
                cur = cur.next
                p2 = p2.next

        return res.next
                

            