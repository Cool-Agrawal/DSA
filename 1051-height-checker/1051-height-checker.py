class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h = sorted(heights)
        c = 0
        for i in range(len(h)):
            if heights[i] != h[i]:
                c += 1
        return c
        