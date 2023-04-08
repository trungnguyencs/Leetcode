class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {num: i for i, num in enumerate(nums2)}
        return [dic[nums1[i]] for i in range(len(nums1))]