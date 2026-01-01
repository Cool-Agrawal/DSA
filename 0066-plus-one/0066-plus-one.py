class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            c = 1
            for i in range(len(digits)-1,-1,-1):
                new = digits[i] + c
                if new == 10:
                    digits[i] = 0
                    c = 1 
                else:
                    digits[i] = new
                    c = 0
                    break
            if c:
                digits.insert(0,1)
            return digits 
