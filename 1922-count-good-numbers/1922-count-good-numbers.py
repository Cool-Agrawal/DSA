class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7 

        if n == 1:
            return 5 % MOD 
        if n % 2 == 0:
            a = n // 2
            
            return (pow(5, a, MOD) * pow(4, a, MOD)) % MOD

        else:
            b = n // 2
            
            return (pow(5, b + 1, MOD) * pow(4, b, MOD)) % MOD 
            