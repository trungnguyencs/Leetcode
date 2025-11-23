class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # if sum mods 3 == 0, then we can just return the sum
        # if sum % 3 == 1, we should remove one smallest element from mod1 or two smallest ones from mod2
        # if sum % 3 == 2, we should remove one smallest element from mod2 or two smallest ones from mod1
        minMod1 = [float('inf'), float('inf')]
        minMod2 = [float('inf'), float('inf')]
        total = 0
        for num in nums:
            total += num
            if num % 3 == 1:
                self.update(num, minMod1)
            elif num % 3 == 2:
                self.update(num, minMod2)
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            return max(total - minMod1[0], total - sum(minMod2))
        else:
            return max(total - minMod2[0], total - sum(minMod1))
            
    def update(self, num, arr):
        if num >= arr[1]:
            return
        elif num < arr[0]:
            arr[0], arr[1] = num, arr[0]
        else:
            arr[1] = num