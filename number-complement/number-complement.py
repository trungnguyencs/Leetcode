class Solution:
    def findComplement(self, num: int) -> int:
        ans = cnt = 0
        while num > 0:
            ans = ans + 2**cnt * (1 - num % 2)
            num //= 2
            cnt += 1
        return ans
        
        # another solution:
        # 8 + 7 = 16 - 1 = 2**4 - 1
        # log(8) = 3
        # return 2**(int(log(num, 2) + 1))-1 - num
        