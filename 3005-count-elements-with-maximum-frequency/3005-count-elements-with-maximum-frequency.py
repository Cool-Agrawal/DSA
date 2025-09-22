from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = Counter(nums)
        a = max(n.values())
        freq = [i for i,j in n.items() if j == a ]
        count = 0
        for i in nums:
            if i in freq:
                count += 1
        return count
        
