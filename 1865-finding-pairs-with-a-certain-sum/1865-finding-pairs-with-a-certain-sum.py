class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counterNums2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        oldVal = self.nums2[index]
        newVal = oldVal + val
        self.counterNums2[oldVal] -= 1
        self.counterNums2[newVal] += 1
        self.nums2[index] = newVal

    def count(self, tot: int) -> int:
        ans = 0
        for num1 in self.nums1:
            ans += self.counterNums2[tot - num1]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)