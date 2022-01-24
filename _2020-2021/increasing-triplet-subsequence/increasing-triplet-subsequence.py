class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # stack-based initial solution:
        # stack = [nums[0]]
        # for num in nums[1:]:
        #     if len(stack) == 1:
        #         if num > stack[-1]:
        #             stack.append(num)
        #         else:
        #             stack[-1] = num
        #     elif len(stack) == 2:
        #         if num > stack[-1]:
        #             return True
        #         elif stack[0] < num <= stack[-1]:
        #             stack[-1] = num
        #         else:
        #             stack[0] = num
        # return False
        
        first = second = float('inf')
        for num in nums:
            if num > second:
                return True
            elif num <= first: # this is to avoid having second == first
                first = num
            elif num < second:
                second = num
        return False
​
