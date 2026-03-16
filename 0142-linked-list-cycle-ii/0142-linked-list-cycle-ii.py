# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        record = set()

        # x = 0
        # while head:
        #     print(head.val)
        #     head = head.next
        #     x += 1
        #     if x == 100:
        #         break

        # return

        
        c = 0
        while head:
            if head in record:
                return head

            record.add(head)
            c += 1

            head = head.next

        