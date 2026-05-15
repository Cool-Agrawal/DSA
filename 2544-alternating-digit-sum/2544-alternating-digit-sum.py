class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a = 0
        s = str(n)
        for i in range(len(s)):
            if i%2 == 0:
                a += int(s[i])
            else:
                a -= int(s[i])
        return a
            