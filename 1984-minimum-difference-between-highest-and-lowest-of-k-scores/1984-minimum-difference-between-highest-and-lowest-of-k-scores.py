class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-k+1):
            c = nums[i+k-1] - nums[i]
            res = min(res,c)
        return res
