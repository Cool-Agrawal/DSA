class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        c = 0
        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                c += 1
                i += 1
                j -= 1
            elif s < k:
                i += 1
            else:
                j -= 1
        return c
        