class Solution:
    def jump(self, nums: List[int]) -> int:
        m = 0
        c = 0
        end = 0
        for i in range(len(nums)-1):
            m = max(m,i+nums[i])
            if i == end:
                c += 1
                end = m
        return c
        