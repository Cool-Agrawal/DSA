class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c = 0
        s = 'aeiou'
        for i in range(left,right+1):
            if words[i][0] in s and words[i][-1] in s:
                c += 1
        return c 

        