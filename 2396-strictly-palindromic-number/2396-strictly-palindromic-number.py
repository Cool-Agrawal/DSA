class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        a = bin(n)
        return str(a) == str(a[::-1])
        