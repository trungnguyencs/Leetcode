class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False
        tipCount = 0
        for i in range(1, len(arr) - 1):
            if arr[i] == arr[i-1] or arr[i] == arr[i+1]:
                return False
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                tipCount += 1
                if tipCount > 1:
                    return False
        return True