class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        if a != 0:
            return len(nums)
        for i in nums:
            if i != 0:
                return len(nums)-1
        return 0
        