class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        a = []
        b = words[0] 
        a.append(b)
        for i in range(1,len(words)):
            if sorted(b) != sorted(words[i]):
                a.append(words[i])
                b = words[i]
            else:
                continue
        #a = sorted(a)
        return a

        