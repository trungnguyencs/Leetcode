class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, count in counter.items():
            if len(heap) < k:
                heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapreplace(heap, (count, num))
        return [num for count, num in heap]