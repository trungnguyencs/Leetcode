class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            idx1, num1 = nums1[i]
            idx2, num2 = nums2[j]
            if idx1 == idx2:
                ans.append([idx1, num1 + num2])
                i += 1
                j += 1
            elif idx1 < idx2:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        while i < len(nums1):
            ans.append(nums1[i])
            i += 1
        while j < len(nums2):
            ans.append(nums2[j])
            j += 1
        return ans