class Solution:
    def minElement(self, nums: List[int]) -> int:
        a = []
        for i in nums:
            s = sum(int(j) for j in str(i))
            a.append(s)
        return min(a)