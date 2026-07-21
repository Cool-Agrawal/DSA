class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        c = 0
        freq = {0:1}
        for i in nums:
            prefix.append(prefix[-1] + i)

        for i in range(1,len(prefix)):
            if prefix[i] - k in freq:
                c += freq[prefix[i]-k]
            if prefix[i] in freq:
                freq[prefix[i]] += 1
            else:
                freq[prefix[i]] = 1
        return c