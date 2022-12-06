class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        return sort(nums)

    def sort(nums):
        if len(nums) ==1:
            return nums
        mid = len(nums)//2
        left = sort(nums[:mid])
        right = sort(nums[mid:])
        return merge_two_lst(left,right)

    def merge_two_lst(left,right):
        c = []
        i = j =0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                c.append(left[i])
                i += 1
            else:
                c.append(right[j])
                j += 1
        if i < len(left):
            c += left[i:]
        if j < len(right):
            c += right[j:]
        return c
