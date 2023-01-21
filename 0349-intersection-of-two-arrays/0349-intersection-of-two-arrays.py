class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [num for num in set(nums1) if num in set(nums2)]