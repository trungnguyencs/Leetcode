class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        costs = deque([(c, i) for i, c in enumerate(costs)])
        frontHeap, backHeap = [], []
        for _ in range(candidates):
            frontHeap.append(costs.popleft())
        for _ in range(candidates):
            if costs:
                backHeap.append(costs.pop())
        heapify(frontHeap); heapify(backHeap)
        for _ in range(k):
            if not backHeap or (frontHeap and frontHeap[0][0] <= backHeap[0][0]):
                ans += heappop(frontHeap)[0]
                if costs:
                    heappush(frontHeap, costs.popleft())
            else:
                ans += heappop(backHeap)[0]
                if costs:
                    heappush(backHeap, costs.pop())
        return ans