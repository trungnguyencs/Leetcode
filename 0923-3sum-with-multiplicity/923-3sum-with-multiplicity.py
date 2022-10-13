class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        self.ans = 0
        for i in range(len(arr) - 2):
            self.helper(arr, i, target)
        return self.ans % (10**9 + 7)
    
    def helper(self, arr, i, target):
        j, k = i + 1, len(arr) - 1
        while j < k:
            s = arr[i] + arr[j] + arr[k]
            if s < target:
                j += 1
            elif s > target:
                k -= 1
            elif arr[j] == arr[k]:
                self.ans += (k - j)*(k - j + 1)//2
                break
            else:
                l = r = 1
                while arr[j] == arr[j+l]: l += 1
                while arr[k] == arr[k-r]: r += 1
                self.ans += l*r
                j, k = j + l, k - r