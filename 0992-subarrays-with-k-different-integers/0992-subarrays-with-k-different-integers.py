class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(nums,k):
            freq = defaultdict(int)
            left = 0
            c = 0
            for right in range(len(nums)):
                freq[nums[right]] += 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                c += (right-left+1)
            return c
        return count(nums,k) - count(nums,k-1)