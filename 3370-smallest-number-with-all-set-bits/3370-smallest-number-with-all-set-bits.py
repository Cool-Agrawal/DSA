class Solution:
    def smallestNumber(self, n: int) -> int:
        a = 1
        while a <= n:
            a*=2
        return a-1