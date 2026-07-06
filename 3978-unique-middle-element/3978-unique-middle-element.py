from collections import Counter
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)//2
        middle = nums[n]
        count = Counter(nums)
        if  count[middle] == 1:
            return True
        return False
        