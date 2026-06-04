class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxend = nums[0]
        max_sum = nums[0]
        minend = nums[0]
        min_sum = nums[0]
        total = nums[0]

        for i in range(1,len(nums)):
            maxend = max(maxend+nums[i],nums[i])
            max_sum = max(max_sum,maxend)
        
            minend = min(minend+nums[i],nums[i])
            min_sum = min(min_sum,minend)

            total += nums[i]
            
        if max_sum < 0:
            return max_sum
            
        return max(max_sum,total - min_sum)