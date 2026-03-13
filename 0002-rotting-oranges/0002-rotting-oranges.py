class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in direction:
                    row = r+dr
                    col = c+dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1

