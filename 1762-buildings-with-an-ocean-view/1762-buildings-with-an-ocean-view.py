class Solution:
    def findBuildings(self, arr: List[int]) -> List[int]:
        ans = [len(arr) - 1]
        maxHeight = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > maxHeight:
                ans.append(i)
                maxHeight = arr[i]
        return reversed(ans)       