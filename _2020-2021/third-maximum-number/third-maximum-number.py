class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        largest = second = third = float('-inf')
        for num in nums:
            if num > largest:
                largest, second, third = num, largest, second
            elif largest > num > second:
                second, third = num, second
            elif second > num > third:
                third = num
        return third if third != float('-inf') else largest