class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        arr = colors + colors[:k-1]
        l = 0
        streak = 1
        ans = 0
        for r in range(1, len(arr)):
            if arr[r] == arr[r-1]:
                streak = 1
                l = r
            else:
                streak += 1
                if streak >= k:
                    ans += 1
        return ans