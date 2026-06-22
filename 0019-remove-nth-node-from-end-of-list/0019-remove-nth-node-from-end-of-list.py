# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        head = ListNode(0, head)

        slow = fast = head
        for i in range(n):
            print(fast)
            fast = fast.next


        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head.next
