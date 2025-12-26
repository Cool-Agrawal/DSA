from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = Counter(nums)
        for i,j in n.items():
            if j == 1:
                return i
        
        