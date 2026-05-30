class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        a = ""
        res = set()
        for i in word:
            if i.isdigit():
                a += i
            else:
                if a:
                    res.add(int(a))
                    a = ""
        if a:
            res.add(int(a))
        return len(res)