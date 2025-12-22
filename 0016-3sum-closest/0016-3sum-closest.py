class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                res.append(total)
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
        if res:
            return min(res,key = lambda x: (abs(x-target),-x))
        return []
        
        