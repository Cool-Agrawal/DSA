class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        for i in s:
            if  i == '#':
                if st:
                    st.pop()
            else:
                st.append(i)
        a = ''.join(st)

        st = []
        for i in t:
            if i == '#':
                if st:
                    st.pop()
            else:
                st.append(i)
        b = ''.join(st)

        return a == b