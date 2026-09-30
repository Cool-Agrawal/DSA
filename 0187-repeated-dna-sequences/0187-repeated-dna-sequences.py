class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        a = set()
        ans = []
        for i in range(len(s)):
            if s[i:i+10] in a and s[i:i+10] not in ans:
                ans.append(s[i:i+10])
            elif i + 10 <= len(s):
                a.add(s[i:i+10])
            
        return ans