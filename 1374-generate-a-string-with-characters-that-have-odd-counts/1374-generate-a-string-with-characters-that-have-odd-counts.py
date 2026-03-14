class Solution:
    def generateTheString(self, n: int) -> str:
        a = 97
        s = ''
        for i in range(n,-1,-1):
            if i%2 !=  0:
                while n>=i:
                    s += chr(a)*i
                    n -= i
                    a += 1
        return s

        