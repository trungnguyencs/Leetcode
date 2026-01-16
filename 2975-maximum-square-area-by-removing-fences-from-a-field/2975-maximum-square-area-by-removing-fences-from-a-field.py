class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        hSet = self.getDistanceSet(hFences + [1, m])
        vSet = self.getDistanceSet(vFences + [1, n])
        for d in sorted(list(hSet), reverse=True):
            if d in vSet: return d**2 % MOD
        return -1
    
    def getDistanceSet(self, arr):
        distances = set()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                distances.add(abs(arr[i] - arr[j]))
        return distances