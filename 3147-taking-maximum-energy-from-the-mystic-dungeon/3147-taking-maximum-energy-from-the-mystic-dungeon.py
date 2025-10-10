class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m = float('-inf')
        n = len(energy)
        for i in range(n - 1, n - k - 1, -1):
            a = 0
            for j in range(i, -1, -k):
                a += energy[j]
                m = max(m, a)
        return m