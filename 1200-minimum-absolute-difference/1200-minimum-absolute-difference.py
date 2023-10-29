class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        ans = []
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d < minDiff:
                minDiff = d
                ans = [[arr[i-1], arr[i]]]
            elif d == minDiff:
                ans.append([arr[i-1], arr[i]])
        return ans