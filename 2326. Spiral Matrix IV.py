# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        i, j = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        while head:
            res[i][j] = head.val
            visited[i][j] = True
            head = head.next

            if not head:
                return res

            di, dj = directions[direction]
            exceed_row = i + di >= m
            exceed_col = j + dj >= n
            if not exceed_row and not exceed_col:
                has_visited = visited[i + di][j + dj]
            else:
                has_visited = True

            if exceed_row or exceed_col or has_visited:
                direction = (direction + 1) % 4
                di, dj = directions[direction]

            i += di
            j += dj

            
        return res
    
"""
Time complexity: O(n)
Space complexity: O(n) (can be improved to O(1) if we don't use visited array and just check if res[i][j] == -1)
"""