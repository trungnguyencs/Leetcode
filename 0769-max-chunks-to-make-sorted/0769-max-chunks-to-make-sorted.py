class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return self.backtrack(arr, 0)
        
    def backtrack(self, arr, i):
        if i == len(arr): return 0
        ans = 1
        for j in range(i, len(arr)):
            if sorted(arr[i:j+1]) == list(range(i, j+1)):
                ans = max(ans, 1 + self.backtrack(arr, j + 1))
        return ans