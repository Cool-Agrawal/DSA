class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        c = 0
        while n!= 0:
            c += n&1
            n >>= 1
        return c
        