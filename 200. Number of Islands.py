class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for n in range(len(grid))]
        num_islands = 0

        def bfs(row, col):
            q = deque([(row, col)])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                (row, col) = q.popleft()
                visited[row][col] = True

                for direction in directions:
                    r, c = row + direction[0], col + direction[1]
                    if (
                        0 <= r < len(grid)
                        and 0 <= c < len(grid[0])
                        and grid[r][c] == "1"
                        and visited[r][c] == False
                    ):
                        q.append((r, c))
                        visited[r][c] = True

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and visited[row][col] == False:
                    bfs(row, col)
                    num_islands += 1

        return num_islands
