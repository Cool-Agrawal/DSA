class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        house2 = nums[0]
        house1 = max(nums[0],nums[1])
        for i in range(2,n):
            curr = max(house1,nums[i]+house2)
            house2 = house1
            house1 = curr
        return house1