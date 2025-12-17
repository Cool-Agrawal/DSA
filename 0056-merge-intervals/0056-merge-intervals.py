class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        j = 0
        res = []
        for i in range(1,len(intervals)):
            if intervals[j][1] >= intervals[i][0]:
                intervals[j][1] = max(intervals[j][1],intervals[i][1])
            else:
                res.append(intervals[j])
                j = i
        res.append(intervals[j])
        return res
        