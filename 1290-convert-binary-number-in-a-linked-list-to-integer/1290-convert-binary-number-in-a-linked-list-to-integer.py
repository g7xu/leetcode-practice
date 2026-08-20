# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binaryList = []
        res = 0
        cur = None

        while head:
            binaryList.append(head.val)
            head = head.next

        for i in range(len(binaryList) - 1, -1, -1):
            
            if cur is None:
                cur = 1
            else:
                cur *= 2

            res += binaryList[i] * cur

        return res 

        