class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        # If at least one number's 3rd bit is 1, then the final result's 3rd bit must be 1
        # If none exists, then if 2nd bit can carry its "1" to the 3rd bit, final result's 3rd bit is also 1
        # If still not, then final result's 3rd bit is 0.
        # Approach: For each bit, count the number of binary "1" on that bit among all numbers. Starting from bit-0. The extra count on bit-0 will then divide by 2 and carry to the count of next bit.
        carry = ans = 0
        for b in range(64):
            # 2 bits 1 at idx i -> 1 bit 1 at idx i + 1
            carry = carry//2 + sum((num>>b) & 1 for num in nums)
            if carry:
                ans |= (1 << b)
        return ans