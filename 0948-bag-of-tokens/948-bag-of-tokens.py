class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens) - 1
        maxScore = score = 0
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                maxScore = max(maxScore, score)
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return maxScore