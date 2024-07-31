class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @cache
        def dp(i):
            if i == len(books): return 0
            width = maxHeight = 0
            ans = float('inf')
            for j in range(i, len(books)):
                if width + books[j][0] > shelfWidth: break
                width += books[j][0]
                maxHeight = max(maxHeight, books[j][1])
                ans = min(ans, maxHeight + dp(j + 1))
            return ans
        
        return dp(0)