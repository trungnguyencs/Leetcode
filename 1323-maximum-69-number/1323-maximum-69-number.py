class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        for i, d in enumerate(digits):
            if d == '6':
                digits[i] = '9'
                break
        return int(''.join(digits))