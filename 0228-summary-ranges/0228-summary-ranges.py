class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        a = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 1:
                if a == nums[i-1]:
                    res.append(str(a))
                    a = nums[i]
                else:
                    res.append(str(a)+'->'+ str(nums[i-1]))
                    a = nums[i]
        if a == nums[-1]:            
            res.append(str(nums[-1]))
        else:
            res.append(str(a)+'->'+str(nums[-1]))
        return res