class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p = [0]*(len(gain)+1)
        p[0] = gain[0]
        for i in range(1,len(gain)):
            p[i] = p[i-1] + gain[i]
        return max(p)
        