class TwoSum:

    def __init__(self):
        self.counter = Counter()

    def add(self, num: int) -> None:
        self.counter[num] += 1

    def find(self, value: int) -> bool:
        for num in self.counter:
            if num == value/2:
                if self.counter[num] > 1:
                    return True
            elif self.counter[value - num] > 0:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)