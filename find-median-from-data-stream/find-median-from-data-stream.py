class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        if not self.minHeap or num >= self.minHeap[0]: 
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        # keep 2 heaps balance: len(minHeap) in [len(maxHeap), len(maxHeap)+1]
        if len(self.minHeap) - len(self.maxHeap) == 2:
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.minHeap) < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        
    def findMedian(self) -> float:
        return (self.minHeap[0] - self.maxHeap[0])/2 if len(self.minHeap) == len(self.maxHeap) else self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()