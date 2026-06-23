# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f and f.next:
            if f.next == s or f.next.next == s:
                return True
            
            f = f.next.next
            s = s.next
        

        return False