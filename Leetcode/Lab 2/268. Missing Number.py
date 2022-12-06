class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        indx_sum = 0
        nums_sum = 0
        for i in range(len(nums)):
            indx_sum += i + 1
            nums_sum += nums[i]

        return indx_sum-nums_sum
