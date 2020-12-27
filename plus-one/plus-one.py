class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while i >= 0 and carry:
            digits[i] += 1
            carry, digits[i] = divmod(digits[i], 10)
            i -= 1
        return [1] + digits if carry == 1 else digits
