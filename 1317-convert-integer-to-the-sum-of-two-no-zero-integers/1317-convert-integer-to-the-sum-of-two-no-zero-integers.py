class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n-1
        while a <= b:
            if a +b == n and '0' not in str(a) and '0' not in str(b):
                return [a,b]
            else:
                a += 1
                b -= 1
         
            
        