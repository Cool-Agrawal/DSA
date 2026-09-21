class Solution:
    def reverseDegree(self, s: str) -> int:
        c = 1
        ans = 0
        for i in s:
            ans += ((ord('z') - ord(i)+ 1)*c)
            c += 1
        return ans