class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        c = 1
        s = 0
        for i in range(n-1,-1,-1):
            if c == 3:
                c = 1
                continue
            else:
                s += cost[i]
                print(s)
            c += 1
        
        return s 
        