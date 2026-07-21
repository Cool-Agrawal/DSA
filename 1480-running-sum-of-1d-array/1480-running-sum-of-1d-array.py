class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[i] + nums[i])
        prefix.pop(0)
        return prefix 
    