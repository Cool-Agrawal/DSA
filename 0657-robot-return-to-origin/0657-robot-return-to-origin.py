class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v = 0
        h = 0
        for i in moves:
            if i == 'R':
                h += 1
            elif i == 'U':
                v += 1
            elif i == 'L':
                h -= 1
            else:
                v -= 1
        return h==0 and v == 0