class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        while k > 0:
            prev = grid[-1][-1]
            for i in range(m):
                for j in range(n):
                    grid[i][j], prev = prev, grid[i][j]
            k -= 1
        return grid
        