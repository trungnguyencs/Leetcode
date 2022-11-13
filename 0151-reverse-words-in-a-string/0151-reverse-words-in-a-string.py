class Solution:
    def reverseWords(self, s: str) -> str:
        arr = self.toList(s)
        self.reverse(arr, 0, len(arr) - 1)
        l = 0
        for r, ch in enumerate(arr):
            if r == len(arr) - 1:
                self.reverse(arr, l, r)
            elif ch == ' ':
                self.reverse(arr, l, r - 1)
                l = r + 1
        return ''.join(arr)
        
    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    def toList(self, s):
        arr = []
        for i, ch in enumerate(s):
            if ch != ' ' or (arr and arr[-1] != ' '):
                arr.append(ch)
        if arr and arr[-1] == ' ':
            arr.pop()
        return arr    