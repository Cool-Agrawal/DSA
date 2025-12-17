class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c = 0
        d = 0
        for i in bills:
            if i == 5:
                c += 1
            if i == 10:
                if c == 0:
                    return False
                d += 1
                c -= 1
            if i == 20:
                if c>0 and d>0:
                    d -= 1
                    c -= 1
                elif c >= 3:
                    c -= 3
                else:
                    return False
        return True
        