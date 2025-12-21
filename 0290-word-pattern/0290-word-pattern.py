class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        ans = defaultdict(list)
        for i in range(len(s)):
            key = pattern[i]
            ans[key].append(s[i])
        res = list(ans.values())

        for i in res:
            if len(set(i)) != 1:
                return False
        m = [i[0] for i in res]
        if len(m) != len(set(m)):
            return False

        return True