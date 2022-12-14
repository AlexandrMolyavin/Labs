def msort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = msort(nums[:mid])
    right = msort(nums[mid:])
    return merge_two_lst(left, right)

def merge_two_lst(left, right):
    c = []
    i = j = 0
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


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = msort(list(set(nums)))
        curLen, maxLen = 1, 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curLen += 1
            else:
                if curLen > maxLen:
                    maxLen = curLen
                curLen = 1

        if curLen > maxLen:
            maxLen = curLen

        return maxLen
