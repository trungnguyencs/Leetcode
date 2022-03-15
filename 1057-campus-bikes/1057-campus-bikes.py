class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # O(wb log(wb)): calculate all distances and sort
        ans = [-1] * len(workers)
        allDistances = sorted([(self.getDistance(worker, bike), w, b) for w, worker in enumerate(workers) for b, bike in enumerate(bikes)])
        takenWorkers, takenBikes = set(), set()
        for d, w, b in allDistances:
            if w in takenWorkers or b in takenBikes: continue
            ans[w] = b
            takenWorkers.add(w)
            takenBikes.add(b)
            if len(takenWorkers) == len(workers): return ans
    
    def getDistance(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])