class HitCounter:

    def __init__(self):
        self.arr = [[0, 0] for _ in range(300)] # [timestamp, count]

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        lastTimestamp = self.arr[i][0]
        if timestamp != lastTimestamp:
            self.arr[i] = [timestamp, 1]
        else:
            self.arr[i][1] += 1

    def getHits(self, timestamp: int) -> int:
        print(self.arr)
        return sum(self.arr[i][1] for i in range(300) if self.arr[i][0] > timestamp - 300)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)