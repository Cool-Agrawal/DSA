class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        s = 1
        m = 1
        if not nums :
            return 0
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] - 1:
                s += 1
                m = max(s,m)
            else:
                s = 1
        return m
        