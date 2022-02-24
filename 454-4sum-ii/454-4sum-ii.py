class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # two dictionaries:
        dic1 = Counter(num1 + num2 for num1 in nums1 for num2 in nums2)
        dic2 = Counter(num3 + num4 for num3 in nums3 for num4 in nums4)
        return sum(dic1[twoSum] * dic2[-twoSum] for twoSum in dic1)
            
        # # one dictionary
        # dic = Counter(num1 + num2 for num1 in nums1 for num2 in nums2)
        # return sum(dic[-num3 - num4] for num3 in nums3 for num4 in nums4)