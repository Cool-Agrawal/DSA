class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = float('inf')
        res = []
        for i in range(1,len(arr)):
            diff = arr[i]-arr[i-1] 
            if diff < m:
                res = [[arr[i-1],arr[i]]]
                m = diff
            elif diff == m:
                res.append([arr[i-1],arr[i]])           
        return res
