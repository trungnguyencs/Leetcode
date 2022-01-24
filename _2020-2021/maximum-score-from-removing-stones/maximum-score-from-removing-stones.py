class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # Assume a <= b <= c
        # Case 1. if a + b >= c. The optimal way is to make pairs between <a, c> and <b, c> where we can get a+b number of pairing
        # Case 2. We can pair all stones of c with stones in a+b, hence we add count of stones in c. The remaining stones of a,b are paired within themselves upon division by 2.
        smallest, middle, largest = sorted([a, b, c])
        if smallest + middle <= largest:
            return smallest + middle
        return largest + (smallest + middle - largest)//2
        