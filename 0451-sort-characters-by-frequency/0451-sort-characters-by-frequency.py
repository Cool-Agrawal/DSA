from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(s)
        a = s.most_common()
        res = ''
        for i in a:
            res += i[0]*i[1]
        return res
