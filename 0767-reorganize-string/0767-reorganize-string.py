class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-freq, c) for c, freq in counter.items()]
        heapify(heap)
        ans = []
        while heap:
            if not ans or heap[0][1] != ans[-1]:
                freq, c = heappop(heap)
                ans.append(c)
                freq += 1
                if freq != 0:
                    heappush(heap, (freq, c))
            elif len(heap) < 2: return ''
            else:
                freq1, c1 = heappop(heap)
                freq2, c2 = heappop(heap)
                ans.append(c2)
                freq2 += 1
                heappush(heap, (freq1, c1))
                if freq2 != 0:
                    heappush(heap, (freq2, c2))
        return ''.join(ans)