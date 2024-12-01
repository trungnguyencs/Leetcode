class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numSet = set()
        for num in arr:
            if num*2 in numSet or (num//2 in numSet and num//2*2 == num):
                return True
            numSet.add(num)
        return False