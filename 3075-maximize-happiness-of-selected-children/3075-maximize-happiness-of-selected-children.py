class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        arr = heapq.nlargest(k, happiness)
        arr.sort(reverse=True)
        ans = t = 0
        for num in arr:
            if num <= t:
                break
            ans += num - t
            t += 1      
        return ans