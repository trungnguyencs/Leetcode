class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def distance(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
        heap = [[0, 0, 0]] # (total distance, worker index, bike-taken state)
        seen = set()
        while heap:
            d, w, bikesTaken = heappop(heap)
            if w == len(workers): return d
            if (w, bikesTaken) in seen: continue
            seen.add((w, bikesTaken))
            for b in range(len(bikes)):
                if (1 << b) & bikesTaken: continue # bike was already taken
                heappush(heap, [d + distance(w, b), w + 1, bikesTaken | (1 << b)])