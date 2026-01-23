class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            while st and i < 0 < st[-1] and st[-1] < abs(i):
                st.pop()
            if st and i < 0 < st[-1] and st[-1] == abs(i):
                st.pop()
            elif not st or i>0 or st[-1] < 0:
                st.append(i)
        return st
