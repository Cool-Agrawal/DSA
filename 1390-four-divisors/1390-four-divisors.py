class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            s = 0
            c = 0
            for j in range(1,int(i**0.5)+1):
                if i%j == 0:
                    s += j
                    c += 1
                    if j != i // j:
                        s += i // j
                        c += 1
                if c > 4:
                    break
            if c == 4:
                res.append(s)
        return sum(res)

        