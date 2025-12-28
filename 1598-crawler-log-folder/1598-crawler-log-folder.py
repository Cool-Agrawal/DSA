class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for i in logs:
            if i == "" or i == "./":
                continue
            if i == "../":
                if st:
                    st.pop()
            else:
                st.append(i)
        return len(st)