class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0: return False
        counter = Counter(hand)
        heap = list(counter.items())
        heapify(heap)
        while heap:
            if len(heap) < W: return False
            tmp = []
            for _ in range(W):
                num, freq = heappop(heap)
                if len(tmp) > 0 and num != tmp[-1][0] + 1: return False
                tmp.append((num, freq - 1))
            while tmp:
                num, freq = tmp.pop()
                if freq > 0:
                    heappush(heap, (num, freq))
        return True