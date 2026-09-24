class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == sum(int(j) for j in str(nums[i])):
                return i
            
        return -1