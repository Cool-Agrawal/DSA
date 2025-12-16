class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if n%2 == 0:
            return True
        return False
        