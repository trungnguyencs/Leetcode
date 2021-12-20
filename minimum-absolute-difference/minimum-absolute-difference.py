class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        minDiff = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff == minDiff:
                ans.append([arr[i-1], arr[i]])
            elif diff < minDiff:
                ans = [[arr[i-1], arr[i]]]
                minDiff = diff
        return ans