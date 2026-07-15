class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        inc = [1]*len(arr)
        dec = [1]*len(arr)

        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                inc[i] = inc[i-1]+1
        
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                dec[i] = dec[i+1] + 1
        
        ans = 0
        for i in range(len(arr)):
            if inc[i] > 1 and dec[i] > 1:
                ans = max(ans,inc[i]+dec[i]-1)
        return ans
        