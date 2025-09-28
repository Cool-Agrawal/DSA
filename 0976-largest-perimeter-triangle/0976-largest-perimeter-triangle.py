class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        m = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] + nums[i] > nums[i+1]:
                m =  nums[i-1] + nums[i] + nums[i+1]
        return m