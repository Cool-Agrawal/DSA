class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        m = 0
        for i in range(n):
            if colors[i] != colors[0]:
                m = max(m,i)
            if colors[i] != colors[n-1-i]:
                m = max(m,n-1-i)
        return m
        