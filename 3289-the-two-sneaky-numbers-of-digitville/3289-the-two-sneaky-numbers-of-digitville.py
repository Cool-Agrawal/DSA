from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = []
        nums = Counter(nums)
        for i,j in nums.items():
            if j == 2:
                a.append(i)
        return a
        