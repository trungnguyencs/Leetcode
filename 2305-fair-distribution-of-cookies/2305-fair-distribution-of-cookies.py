class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans = float('inf')
        self.backtrack(cookies, [0]*k, 0)
        return self.ans
        
    def backtrack(self, cookies, arr, i):
        if i == len(cookies):
            self.ans = min(self.ans, max(arr))
            return
        # early stop
        if arr.count(0) > len(cookies) - i: return  
        if max(arr) >= self.ans: return
        for j in range(len(arr)):
            arr[j] += cookies[i]
            self.backtrack(cookies, arr, i+1)
            arr[j] -= cookies[i]