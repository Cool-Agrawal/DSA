class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            res = max(res,prod)
            if prod == 0:
                prod = 1
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            prod *= nums[i]
            res = max(res,prod)
            if prod == 0:
                prod = 1   
        return res