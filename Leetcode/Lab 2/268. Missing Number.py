class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        for i in range(0,len(nums)):
            if i not in nums:
                return i
        return i+1