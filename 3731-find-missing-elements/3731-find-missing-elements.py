class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = set(range(min(nums),max(nums)+1))
        num = set(nums)
        return sorted(list(a-num))
        