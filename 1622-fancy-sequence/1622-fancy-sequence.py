class Fancy:

    def __init__(self):
        self.a = []
        self.add = 0
        self.mul = 1
        self.mod = 10**9 + 7

    def append(self, val: int) -> None:
        val = (val - self.add) * pow(self.mul, -1, self.mod)
        val %= self.mod
        self.a.append(val)
        

    def addAll(self, inc: int) -> None:
        self.add = (self.add+inc)%self.mod
        

    def multAll(self, m: int) -> None:
        self.mul = (self.mul*m)%self.mod
        self.add = (self.add*m)%self.mod

    def getIndex(self, idx: int) -> int:
        if idx < len(self.a):
            return (self.a[idx]*self.mul + self.add) % self.mod
        return -1
       

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)