class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        ans = float('-inf')
        s = 0
        # sort nums2 then iterate, the multiplier will be decreasing
        for num2, num1 in sorted(list(zip(nums2, nums1)), reverse=True):
            if len(heap) < k:
                s += num1
                heappush(heap, num1)
                if len(heap) == k:
                    ans = s * num2
            elif heap[0] < num1:
                s += num1 - heappop(heap)
                heappush(heap, num1)
                ans = max(ans, s * num2)
        return ans