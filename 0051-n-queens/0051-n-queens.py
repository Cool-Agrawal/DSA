class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'for i in range(n)] for j in range(n)]
        def backtrack(row):
            if row == n:
                res.append(["".join(i) for i in board])
            for col in range(n):
                if isSafe(row,col):
                    board[row][col] = 'Q'
                    backtrack(row+1)
                    board[row][col] = '.'

        def isSafe(row,col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            for i in range(1,min(row,col)+1):
                if board[row-i][col-i] == 'Q':
                    return False
            for i in range(1,min(row,n-1-col)+1):
                if board[row-i][col+i] == 'Q':
                    return False
            return True
        backtrack(0)
        return res