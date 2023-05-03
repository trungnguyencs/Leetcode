class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uniq1, uniq2 = set(nums1), set(nums2)
        return [(num1 for num1 in uniq1 if num1 not in uniq2), (num2 for num2 in uniq2 if num2 not in uniq1)]