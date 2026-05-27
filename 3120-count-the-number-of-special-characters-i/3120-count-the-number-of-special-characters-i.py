class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        s = set()
        c = 0
        for i in word:
            if ord(i)+32 in s or ord(i)-32 in s:
                c += 1
            else:
                s.add(ord(i))
        return c