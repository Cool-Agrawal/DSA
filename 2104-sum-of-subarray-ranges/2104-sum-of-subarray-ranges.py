class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            m = nums[i]
            n = nums[i]
            for j in range(i,len(nums)):
                m = max(m,nums[j])
                n = min(n,nums[j])
                c += m-n
        return c
