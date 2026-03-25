# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# go over each node in the linkedist

# if only one exist, use that one
# if both sum them up, keep the last, and other as place holder


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        res = head

        pre = 0
        while l1 or l2:
            cur = pre

            if l1:
                cur += l1.val
                l1 = l1.next

            if l2:
                cur += l2.val
                l2 = l2.next

            if cur >= 10:
                res.next = ListNode(int(str(cur)[-1]))
                pre = int(str(cur)[:-1])
            else:
                res.next = ListNode(cur)
                pre = 0

            res = res.next

        if pre:
            res.next = ListNode(pre)

        return head.next
        
            
