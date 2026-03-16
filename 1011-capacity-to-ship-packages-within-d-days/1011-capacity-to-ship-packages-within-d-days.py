class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = high
        while low <= high:
            mid = (low+high)//2
            ship = 1
            curr = 0
            for i in weights:
                if i+curr > mid:
                    ship += 1
                    curr = i
                else:
                    curr += i
            if ship <= days:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res