class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        heap = [[0, 0, 0]] # (total distance, worker index, bike-taken state)
        seen = set()
        while heap:
            d, w, bikesTaken = heappop(heap)
            if w == len(workers): return d
            if (w, bikesTaken) in seen: continue
            seen.add((w, bikesTaken))
            for b in range(len(bikes)):
                if (1 << b) & bikesTaken: continue # bike was already taken
                heappush(heap, [d + self.distance(workers[w], bikes[b]), w + 1, bikesTaken | (1 << b)])
                
    def distance(self, ptA, ptB):
        return abs(ptA[0] - ptB[0]) + abs(ptA[1] - ptB[1])