class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        XMinusY = sum(nums) - n*(n + 1)//2
        XSquareMinusYSquare = sum(x**2 for x in nums) - n*(n + 1)*(2*n + 1)//6
        XPlusY = XSquareMinusYSquare//XMinusY
        return (XPlusY + XMinusY)//2, (XPlusY - XMinusY)//2