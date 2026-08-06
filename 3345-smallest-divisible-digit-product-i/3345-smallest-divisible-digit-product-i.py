class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            prod = 1
            for j in str(i):
                prod *= int(j)
            if prod % t == 0:
                return i
        