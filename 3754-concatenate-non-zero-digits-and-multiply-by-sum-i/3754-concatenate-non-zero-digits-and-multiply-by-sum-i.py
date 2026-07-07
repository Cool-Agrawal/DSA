class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ""
        for i in str(n):
            if i in "123456789":
                s += i
        if not s:
            return 0
        x = int(s)
        sum_digit = sum(int(i) for i in s)
        return sum_digit*x
        