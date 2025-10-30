class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        c = target[0]
        for i in range(1,len(target)):
            if target[i] > target[i-1]:
                c += target[i]-target[i-1]
        print(c)
        return c
        