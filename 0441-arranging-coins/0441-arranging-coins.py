class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        c = 0
        while k <= n:
            n -= k
            k += 1
            c += 1
        return c
        