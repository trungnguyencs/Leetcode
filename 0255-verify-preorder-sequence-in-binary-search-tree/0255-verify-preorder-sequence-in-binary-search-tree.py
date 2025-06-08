class Solution:
    '''
    #Using array slicing will time out
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self.helper(preorder, lBound=-float('inf'), rBound=float('inf'))

    def helper(self, arr, lBound, rBound):
        if not arr: return True
        root = arr[0]
        if not lBound < root < rBound: return False
        # Find the first index where the value is greater than root (start of right subtree)
        rightStart = 1
        while rightStart < len(arr) and arr[rightStart] < root:
            rightStart += 1
        return self.helper(arr[1:rightStart], lBound, root) and self.helper(arr[rightStart:], root, rBound)
    '''
    #Using array slicing will time out, so need to pass start index and end index into helper method instead
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self.helper(preorder, start=0, end=len(preorder)-1, lBound=-float('inf'), rBound=float('inf'))

    def helper(self, arr, start, end, lBound, rBound):
        if start > end: return True
        root = arr[start]
        if not lBound < root < rBound: return False
        # Find the first index where the value is greater than root (start of right subtree)
        rightStart = start + 1
        while rightStart <= end and arr[rightStart] < root:
            rightStart += 1
        return self.helper(arr, start + 1, rightStart - 1, lBound, root) and self.helper(arr, rightStart, end, root, rBound)