class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxend = arr[0]
        ans = 0
        res = arr[0]
        for i in range(1,len(arr)):
            ans = max(maxend,ans+arr[i])
            maxend = max(arr[i],maxend+arr[i])
            res = max(res,ans,maxend)
        return res
        