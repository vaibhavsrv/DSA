class Fancy:

    def __init__(self):
        self.start = 1
        self.end = 0
        self.vals = []
        self.MOD = 10**9+7

    def append(self, val: int) -> None:
        x = (val - self.end) % self.MOD
        x = x*pow(self.start,self.MOD-2,self.MOD) % self.MOD
        self.vals.append(x)

    def addAll(self, inc: int) -> None:
        self.end = (self.end+inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.start = (self.start * m) % self.MOD
        self.end = (self.end * m) % self.MOD
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        else:
            return (self.start * self.vals[idx] + self.end) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)