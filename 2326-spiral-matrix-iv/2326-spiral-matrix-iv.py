# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        m_dir = [
            [0, 1], [1, 0], [0, -1], [-1, 0]
        ]
        cur_m = 0

        x = y = 0
        
        res = [[-1] * n for _ in range(m)]
        filled = set()
        while head:
            res[x][y] = head.val
            filled.add((x, y))

            nx = x + m_dir[cur_m][0]
            ny = y + m_dir[cur_m][1]

            if nx < 0 or nx >= len(res) or ny < 0 or ny >= len(res[nx]) or (nx, ny) in filled:
                cur_m = (cur_m + 1) % 4
                nx = x + m_dir[cur_m][0]
                ny = y + m_dir[cur_m][1]

            x, y = nx, ny

            head = head.next

        return res