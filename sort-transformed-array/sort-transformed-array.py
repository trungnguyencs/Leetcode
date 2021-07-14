class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        ans = []
        l, r, i = 0, len(nums) - 1, 0
        if a >= 0:
            while l <= r:
                left, right = self.quad(nums[l], a, b, c), self.quad(nums[r], a, b, c)
                if left > right:
                    ans.append(left)
                    l += 1
                else:
                    ans.append(right)
                    r -= 1
            return ans[::-1]
        else:
            while l <= r:
                left, right = self.quad(nums[l], a, b, c), self.quad(nums[r], a, b, c)
                if left < right:
                    ans.append(left)
                    l += 1
                else:
                    ans.append(right)
                    r -= 1
            return ans
    
    def quad(self, x, a, b, c):
        return a*x**2 + b*x + c