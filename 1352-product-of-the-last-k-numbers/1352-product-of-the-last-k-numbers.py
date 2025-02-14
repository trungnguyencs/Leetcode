class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(num * self.arr[-1])

    def getProduct(self, k: int) -> int:
        #len(self.arr) == k means there's k-1 numbers since last zero
        if len(self.arr) <= k: return 0
        return self.arr[-1]//self.arr[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)