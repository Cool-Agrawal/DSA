class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist = 0
        c = 0
        for i in moves:
            if i == 'R':
                dist += 1
            elif i == 'L':
                dist -= 1
            else:
                c += 1
        return abs(dist+c) if dist > 0 else abs(dist-c)
        