from bisect import bisect_left

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices, maxBeauty = zip(*items)
        prices, maxBeauty = list(prices), list(maxBeauty)
        for i in range(1, len(maxBeauty)):
            maxBeauty[i] = max(maxBeauty[i], maxBeauty[i-1])
        ans = []
        for maxPrice in queries:
            i = bisect_right(prices, maxPrice)
            if i == 0:
                ans.append(0)
            else:
                ans.append(maxBeauty[i-1])
        return ans