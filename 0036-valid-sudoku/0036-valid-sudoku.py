class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        row = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        column = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        block = [[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]

        for i in range(9):
            for j in range(9):
                if b[i][j] == '.':
                    continue
                if b[i][j] in row[i]:
                    return False
                row[i].add(b[i][j])

                if b[i][j] in column[j]:
                    return False
                column[j].add(b[i][j])

                if b[i][j] in block[i//3][j//3]:
                    return False
                block[i//3][j//3].add(b[i][j])
        
        return True