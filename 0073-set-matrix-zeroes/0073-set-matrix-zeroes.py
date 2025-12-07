class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z_row = set()
        z_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    z_row.add(i)
                    z_col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in z_row or j in z_col:
                    matrix[i][j] = 0
        return matrix
        