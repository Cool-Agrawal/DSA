class Solution:
    def mySqrt(self, x: int) -> int:
        r = 1
        while r*r <= x :
            r += 1
        return r-1

        