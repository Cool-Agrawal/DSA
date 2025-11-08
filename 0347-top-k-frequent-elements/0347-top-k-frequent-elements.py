from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        nums = Counter(nums)
        num = nums.most_common()
        for i in num:
            if k:
                a.append(i[0])
                k -= 1
            else:
                break
        return a
        
        