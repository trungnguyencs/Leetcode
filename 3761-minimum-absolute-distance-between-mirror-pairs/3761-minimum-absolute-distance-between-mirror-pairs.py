class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        futureRev = {}
        ans = float('inf')
        for i, num in enumerate(nums):
            if num in futureRev:
                ans = min(ans, i - futureRev[num])
            rev = int(str(num)[::-1])
            futureRev[rev] = i
        return -1 if ans == float('inf') else ans