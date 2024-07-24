class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return [nums[i] for i in sorted(range(len(nums)), key=lambda i: (self.convert(nums[i], mapping), i))]
        
    def convert(self, num, mapping):
        if num == 0: return mapping[0]
        convertedNum = i = 0
        while num:
            num, d = divmod(num, 10)
            convertedNum += mapping[d] * 10**i
            i += 1
        return convertedNum