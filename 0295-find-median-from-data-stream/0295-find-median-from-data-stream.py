class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # stores smaller numbers
        self.minHeap = [] # stores bigger numbers

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or num >= self.minHeap[0]:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        if len(self.minHeap) - len(self.maxHeap) == 2:
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) == 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:
        return (self.minHeap[0] - self.maxHeap[0])/2 if len(self.maxHeap) == len(self.minHeap) else self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()