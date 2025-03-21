class StockPrice:

    def __init__(self):
        self.lastTime = 0
        self.dic = {}
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.dic[timestamp] = price
        self.lastTime = max(self.lastTime, timestamp)
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.dic[self.lastTime]

    def maximum(self) -> int:
        while self.dic[self.maxHeap[0][1]] != -self.maxHeap[0][0]: #meaning this price has been overwritten
            heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.dic[self.minHeap[0][1]] != self.minHeap[0][0]: #meaning this price has been overwritten
            heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()