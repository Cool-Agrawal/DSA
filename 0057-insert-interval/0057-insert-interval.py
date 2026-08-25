class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []

        for i, j in intervals:

            if j < newInterval[0]:
                ans.append([i, j])

            elif i > newInterval[1]:
                ans.append(newInterval)
                newInterval = [i, j]

            else:
                newInterval[0] = min(newInterval[0], i)
                newInterval[1] = max(newInterval[1], j)

        ans.append(newInterval)

        return ans