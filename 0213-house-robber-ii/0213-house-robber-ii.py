class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        return max(self.stick(nums[:-1]),self.stick(nums[1:]))

    def stick(self,arr):
        house2 = 0
        house1 = 0
        for i in arr:
            curr = max(house1,i+house2)
            house2 = house1
            house1 = curr
        return house1
        