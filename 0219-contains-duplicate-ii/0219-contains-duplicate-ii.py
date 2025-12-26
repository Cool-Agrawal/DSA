class Solution:
    def containsNearbyDuplicate(self, ns: List[int], k: int) -> bool:
        s = {}
        for i in range(len(ns)):
            if ns[i] in s:
                for j in s[ns[i]]:
                    if abs(i - j) <= k:
                        return True
                s[ns[i]].append(i)
            else:
                s[ns[i]] = [i]
        
        return False