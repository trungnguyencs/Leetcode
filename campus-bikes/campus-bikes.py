class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        ans = [-1]*len(workers)
        dic = defaultdict(list)
        for w, worker in enumerate(workers):
            for b, bike in enumerate(bikes):
                dic[w].append([self.getDistance(worker, bike), w, b])
            dic[w].sort(reverse=True)
        takenBikes = set()
        heap = [dic[w].pop() for w in range(len(workers))]
        heapify(heap)
        while heap:
            d, w, b = heappop(heap)
            if b in takenBikes:
                heappush(heap, dic[w].pop())
            else:
                ans[w] = b
                takenBikes.add(b)
        return ans
                
    def getDistance(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])