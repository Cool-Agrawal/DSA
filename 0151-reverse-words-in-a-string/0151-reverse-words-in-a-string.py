class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a.reverse()
        b = ""
        for i in range(len(a)):
            if i != len(a)-1:
                b += a[i] + " "
            else:
                b += a[i]
        return b