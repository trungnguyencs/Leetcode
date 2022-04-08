class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.helper(self.heap, self.k, num)
        
    def add(self, num: int) -> int:
        self.helper(self.heap, self.k, num)
        return self.heap[0]
    
    def helper(self, heap, k, num):
        if len(heap) < k:
            heappush(heap, num)
        elif num > heap[0]:
            heapreplace(heap, num)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)