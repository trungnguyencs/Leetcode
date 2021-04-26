class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = list(map(int, version1.split('.')))
        nums2 = list(map(int, version2.split('.')))
        if len(nums1) < len(nums2): nums1 += [0]*(len(nums2) - len(nums1))
        else: nums2 += [0]*(len(nums1) - len(nums2))
        for i in range(len(nums1)):
            if nums1[i] < nums2[i]: return -1
            elif nums1[i] > nums2[i]: return 1
        return 0