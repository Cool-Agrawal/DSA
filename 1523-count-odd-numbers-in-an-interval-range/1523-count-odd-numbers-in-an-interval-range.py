class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high-low+1
        if total %2 == 0:
            return total//2
        else:
            if low%2 == 1 or high%2 == 1:
                return total//2 + 1
        return total//2
        