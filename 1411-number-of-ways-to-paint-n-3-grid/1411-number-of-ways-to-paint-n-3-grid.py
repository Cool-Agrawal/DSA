class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        a = 6
        b = 6
        for i in range(2,n+1):
            x = (3*a + 2*b)%mod
            y = (2*a + 2*b)%mod
            a,b = x,y
        return (a+b)%mod