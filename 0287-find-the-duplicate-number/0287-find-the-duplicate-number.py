from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for i,j in nums.items():
            if j > 1:
                return i
