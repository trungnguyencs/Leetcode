class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = removed = 0
        for count in sorted(counter.values(), reverse=True):
            removed += count
            ans += 1
            if removed >= len(arr)/2: break
        return ans