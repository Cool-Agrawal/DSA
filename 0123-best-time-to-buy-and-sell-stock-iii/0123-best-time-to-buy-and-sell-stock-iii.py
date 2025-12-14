class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        p1 = 0
        buy2 = float('inf')
        p2 = 0
        for i in prices:
            buy1 = min(buy1,i)
            p1 = max(p1,i-buy1)
            buy2 = min(buy2,i-p1)
            p2 = max(p2,i-buy2)
        return p2        