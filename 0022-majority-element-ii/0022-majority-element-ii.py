from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        res = []
        for i,j in nums.items():
            if j > n//3:
                res.append(i)
        return res

        