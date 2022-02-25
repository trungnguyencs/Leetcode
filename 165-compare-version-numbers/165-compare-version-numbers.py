class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = list(map(int, version1.split('.')))
        arr2 = list(map(int, version2.split('.')))
        for i in range(max(len(arr1), len(arr2))):
            curNum1 = arr1[i] if i < len(arr1) else 0
            curNum2 = arr2[i] if i < len(arr2) else 0
            if curNum1 < curNum2: return -1
            if curNum1 > curNum2: return 1
        return 0