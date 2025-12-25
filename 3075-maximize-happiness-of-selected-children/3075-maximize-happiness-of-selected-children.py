class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        s = 0
        for i in range(k):
            val = max(0,happiness[i]-i)
            s += val
        return s

        