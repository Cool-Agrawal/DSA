class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(1,500):
            if i%k == 0 and i not in nums:
                s = i
                break
        return s
        