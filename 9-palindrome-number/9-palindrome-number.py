class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0: return False
        numCopy, reversedNum = num, 0
        while numCopy:
            reversedNum = reversedNum * 10 + numCopy % 10
            numCopy //= 10
        return reversedNum == num