class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            if len(heap) < k:
                heappush(heap, (freq, num))
            elif freq >= heap[0][0]:
                heapreplace(heap, (freq, num))
        return [num for _, num in heap]