class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        c = 0
        for i in range(len(num)-1,-1,-1):
            new = num[i] + k%10 + c
            if new > 9:
                num[i] = new % 10
                c = 1
            else:
                num[i] = new
                c = 0
            k //= 10
        k = k+c
        while k :
            num.insert(0,k%10)
            k //= 10
        return num
        