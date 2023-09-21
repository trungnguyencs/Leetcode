class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i1 = i2 = prev = cur = 0
        for i in range((len1 + len2)//2 + 1):
            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] < nums2[i2]:
                    cur = nums1[i1]
                    i1 += 1
                else:
                    cur = nums2[i2]
                    i2 += 1
            elif i1 < len(nums1):
                cur = nums1[i1]
                i1 += 1
            else:
                cur = nums2[i2]
                i2 += 1
            if i == (len1 + len2)//2 - 1: prev = cur
        return cur if (len1 + len2) % 2 == 1 else (prev + cur)/2