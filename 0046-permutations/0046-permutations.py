class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(start):
            if start == len(nums):
                res.append(nums[:])
                return 
            for i in range(start,len(nums)):
                nums[start],nums[i] = nums[i],nums[start]
                solve(start+1)
                nums[start],nums[i] = nums[i],nums[start]
        solve(0)
        return res

        