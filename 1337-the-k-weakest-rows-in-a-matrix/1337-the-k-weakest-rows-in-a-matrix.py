class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = [] # max heap to replace the biggest rank in the heap
        for i, row in enumerate(mat):
            rank = self.getRank(row)
            if len(heap) < k:
                heappush(heap, (-rank, -i))
            elif rank < -heap[0][0]:
                heapreplace(heap, (-rank, -i))
        return [-i for _, i in sorted(heap, reverse=True)]
        
    def getRank(self, row):
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r)//2
            if row[m] == 1 and (m == len(row) - 1 or row[m+1] == 0):
                return m
            if row[m] == 1:
                l = m + 1
            else:
                r = m - 1
        return -1