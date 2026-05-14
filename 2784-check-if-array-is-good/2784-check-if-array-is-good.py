from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)-1
        num = Counter(nums)
        for i in range(1,n):
            if num[i] != 1:
                return False
        if num[n] != 2:
            return False
        return True
        