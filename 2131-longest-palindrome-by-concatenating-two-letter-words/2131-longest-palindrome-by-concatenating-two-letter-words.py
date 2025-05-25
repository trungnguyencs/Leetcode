class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        oddSeen = False
        counter = Counter(words)
        ans = 0
        for w, freq in counter.items():
            a, b = w[0], w[1]
            if a == b:
                if freq % 2 == 0:
                    ans += freq
                elif oddSeen:
                    ans += freq - 1
                else:
                    ans += freq
                    oddSeen = True
            else:
                ans += min(freq, counter[b + a])
        return ans * 2