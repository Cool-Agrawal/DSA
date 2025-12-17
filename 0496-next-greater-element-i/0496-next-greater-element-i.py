class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        ans = [-1]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and st[-1] < nums2[i]:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(nums2[i])
        res = []
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    res.append(ans[j])
                    break
                
        return res


        