class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, count1, count2 = -1, -1, 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = num, 1
            elif count2 == 0:
                num2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        if nums.count(num1) > len(nums)//3:
            ans.append(num1)
        if num2 != num1 and nums.count(num2) > len(nums)//3:
            ans.append(num2)
        return ans