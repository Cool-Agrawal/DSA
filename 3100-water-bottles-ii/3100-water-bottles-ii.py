class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        b = numBottles
        e = numBottles
        while e>= numExchange:
            e -= numExchange
            numExchange += 1
            b += 1
            e += 1
        return b