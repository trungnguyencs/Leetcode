class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        ans = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            m = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == arr2[j] == arr3[k]:
                ans.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] == m:
                i += 1
            elif arr2[j] == m:
                j += 1
            else:
                k += 1
        return ans