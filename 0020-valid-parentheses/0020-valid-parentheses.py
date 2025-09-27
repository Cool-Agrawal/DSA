class Solution:
    def isValid(self, s: str) -> bool:
        
        a = []
      
        for i in s:
            if i == "(" or i == "{" or i == "[":
                a.append(i)
            
            else:
                if a and ((i == ")" and a[-1] == "(" ) or (i == "]" and a[-1] == "[") or (i == "}" and a[-1] == "{")):
                    a.pop()
                else:
                    return False
        return len(a) == 0
        