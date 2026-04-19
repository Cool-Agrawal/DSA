class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        res = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                a = j-i
                res = max(a,res)
                j += 1
            else:
                i += 1
        return res


        