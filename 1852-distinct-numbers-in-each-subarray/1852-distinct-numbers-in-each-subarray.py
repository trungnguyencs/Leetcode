class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums[:k])
        ans = [len(counter)]
        for i in range(k, len(nums)):
            cur, prev = nums[i], nums[i-k]
            counter[cur] += 1
            counter[prev] -= 1
            if counter[prev] == 0:
                del counter[prev]
            ans.append(len(counter))
        return ans