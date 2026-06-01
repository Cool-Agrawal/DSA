class Solution:
    def myAtoi(self, s: str) -> int:
        a = ""
        sign = 1
        for i in s:
            if i == " " and a == "":
                continue
            elif i.isdigit():
                a += i
                print(a)
            elif i == '-' and a == "":
                sign = -1
                a += '0'
            elif i == '+' and a == "":
                sign = 1
                a += '0'
            else:
                break

        if a=='' or a == '0':
            return 0

        res = int(a)*sign   

        if res < -2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1    

        return res 
        