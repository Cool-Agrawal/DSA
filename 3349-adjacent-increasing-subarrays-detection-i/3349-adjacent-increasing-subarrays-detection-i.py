class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        a = k-1
        for i in range(k+1,len(nums)): 
            if a == 0:
                return True 
            if nums[i - 1] < nums[i] and nums[i - 1 - k] < nums[i - k]:
                a -= 1
            else:
                a = k-1
                
        return a == 0
                
        