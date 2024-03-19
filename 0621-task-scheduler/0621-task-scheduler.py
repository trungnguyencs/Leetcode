class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-freq for freq in counter.values()]
        heapify(heap)
        ans = 0
        while heap:
            tmp = []
            for _ in range(n + 1):
                if heap:
                    freq = -heappop(heap)
                    freq -= 1
                    if freq > 0: tmp.append(freq)
                ans += 1
                if not heap and not tmp: return ans
            for freq in tmp:
                heappush(heap, -freq)
        return ans