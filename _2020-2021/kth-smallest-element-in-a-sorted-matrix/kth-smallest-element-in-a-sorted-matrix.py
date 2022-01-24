class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [[row[0], r, 0] for r, row in enumerate(matrix)]
        heapify(heap)
        while k > 0:
            num, r, c = heappop(heap)
            if c < len(matrix) - 1:
                heappush(heap, [matrix[r][c+1], r, c + 1])
            k -= 1
        return num