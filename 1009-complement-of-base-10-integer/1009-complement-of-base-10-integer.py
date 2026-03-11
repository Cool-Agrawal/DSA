class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        def msb(n):
            count = 0
            while n!=0:
                n = n >> 1
                count += 1
            return count
        return n^((1 << msb(n))-1)
    
        