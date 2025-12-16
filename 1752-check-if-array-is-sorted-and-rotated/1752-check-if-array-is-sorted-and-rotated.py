class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        temp = arr + arr
        n = len(nums)
        for i in range(len(temp)):
            if temp[i:i+n] == nums:
                return True
        return False
        