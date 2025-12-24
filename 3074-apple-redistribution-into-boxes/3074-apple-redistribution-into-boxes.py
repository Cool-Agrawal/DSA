class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a = sum(apple)
        capacity.sort(reverse = True)
        s = 0
        c = 0
        for i in capacity:
            if s >= a:
                return c
            s += i
            c += 1
        return len(capacity)