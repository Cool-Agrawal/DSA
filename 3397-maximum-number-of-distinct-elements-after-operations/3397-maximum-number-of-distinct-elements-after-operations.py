class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        a = set()
        l = float('-inf')

        for i in nums:
            val = max(i - k, l + 1)
            if val <= i + k:
                a.add(val)
                l = val

        return len(a)
