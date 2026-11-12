class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c = 1
        m = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                c += 1
            else:
                c = 1
            m = max(c,m)
        n = 1
        d = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                d += 1
            else:
                d = 1
            n = max(d,n)
        return max(m,n)
        