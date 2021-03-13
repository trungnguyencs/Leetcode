class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pt in points:
            dis = pt[0]**2 + pt[1]**2
            if len(heap) < k:
                heappush(heap, (-dis, pt))
            elif dis < -heap[0][0]:
                heapreplace(heap, (-dis, pt))
        return [element[1] for element in heap]