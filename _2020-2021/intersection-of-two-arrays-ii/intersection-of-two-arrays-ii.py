class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = {}
        for num in nums1:
            if num not in counter:
                counter[num] = [0, 0]
            counter[num][0] += 1
        for num in nums2:
            if num in counter:
                counter[num][1] += 1
        return [k for k, v in counter.items() for freq in range(min(v))]