from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        a = []
        for i,j in nums.items():
            if j == 2:
                a.append(i)
        a.sort()
        return a