#/ *Merge * /


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
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

#/ *Fast * /


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        elem = nums[0]
        left = list(filter(lambda x: x < elem, nums))
        center = [i for i in nums if i == elem]
        right = list(filter(lambda x: x > elem, nums))

        return self.sortArray(left) + center + self.sortArray(right)
