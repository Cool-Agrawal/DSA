class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        if nums[0] == 0:
            return False
        if nums[1] > nums[0]:
            a = nums[1]
            b = len(nums)-2
        else:
            a = nums[0]
            b = len(nums)-1
        
        print(a,b)
        if a >= b:
            return True
        return False
        