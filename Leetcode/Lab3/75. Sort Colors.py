def merge_two_lst(left, right):
    class Solution:
        def sortColors(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            count = [0] * 3
            for i in range(len(nums)):
                count[nums[i]] += 1
            nums.clear()
            for i in range(len(count)):
                while count[i] > 0:
                    nums.append(i)
                    count[i] -= 1