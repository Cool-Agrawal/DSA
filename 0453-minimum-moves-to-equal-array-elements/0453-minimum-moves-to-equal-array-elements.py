class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a = min(nums)
        c = 0
        for i in nums:
            c += i-a
        return c
            

        