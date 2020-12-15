class MedianFinder:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
​
    def addNum(self, num: int) -> None:
        if not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        # 0 <= len(minHeap) - len(maxHeap) <= 1
        if len(self.minHeap) - len(self.maxHeap) == 2:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) == 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2
        return self.minHeap[0]
​
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
