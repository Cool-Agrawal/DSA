class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            r,c = q.popleft()
            for i,j in directions:
                row = r+i
                col = c+j
                if row<0 or row>=rows or col<0 or col>=cols:
                    continue
                if mat[row][col] == -1:
                    mat[row][col] = mat[r][c] + 1
                    q.append((row,col))
        return mat

                
        

        