class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        #1st approach - Loi giai sai:
        left, right = 0, len(nums) - 1
        for mid in range(len(nums)):
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
            elif nums[mid] == 2:
                #sai cho nay vi ta khong biet nums[right] la gi
                #neu la 2 thi so 2 nay se bi swap ra giua, truoc cac so 1 sau nay
                #neu la 0 thi so 0 nay co the dung sau cac so 1 truoc do
                #nhu vay neu nums[mid] == 2 thi ko duoc move mid
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        """
        #Loi giai dung:
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1