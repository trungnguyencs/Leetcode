class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num  # keep the stack monotonic decreasing
            stack.append(num)
        return [dic.get(num, -1) for num in nums1]
        