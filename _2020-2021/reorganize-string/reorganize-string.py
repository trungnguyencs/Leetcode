class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        counter = Counter(s)
        heap = [(-count, ch) for ch, count in counter.items()]
        heapify(heap)
        # the only case that we can not rearrange is when a character appears more than half of (len(s) + 1)
        if -heap[0][0] > (len(s) + 1)//2: return ''
        while len(heap) > 1:
            countM, more = heappop(heap)
            countL, less = heappop(heap)
            ans += [more, less]
            if countM != -1:
                heappush(heap, (countM + 1, more))
            if countL != -1:
                heappush(heap, (countL + 1, less))
        return ''.join(ans) if len(heap) == 0 else ''.join(ans + [heap[0][1]])