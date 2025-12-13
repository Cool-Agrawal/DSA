class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        j = 0
        for i in range(len(magazine)):
            if ransomNote[j] == magazine[i]:
                j += 1
            if j == len(ransomNote):
                return True
        return False


        