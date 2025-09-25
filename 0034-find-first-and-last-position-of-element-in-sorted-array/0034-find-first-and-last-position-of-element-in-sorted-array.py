class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                break
        a = 0
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
        res.append(a)
        if res != [0]:
            return res
    
        return [-1,-1]

        

        