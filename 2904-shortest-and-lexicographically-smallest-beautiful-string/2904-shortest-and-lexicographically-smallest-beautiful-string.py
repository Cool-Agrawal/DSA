class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        st = []
        res = []
        c = 0
        for i in s:
            st.append(i)
            if i == '1':
                c += 1
            while c == k:
                res.append("".join(st))
                if st.pop(0) == '1':
                    c -= 1
        if not res:
            return ""

        return min(res,key = lambda x: (len(x),x))
            
        