class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        ln = len(nums)
        for i in range(ln - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[ln - 3] + nums[ln - 2] + nums[ln - 1] < target:
                continue

            for j in range(i + 1, ln - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[ln - 2] + nums[ln - 1] < target:
                    continue

                low, high = j + 1, ln - 1
                while low < high:
                    distance = nums[i] + nums[j] + nums[low] + nums[high] - target
                    if distance == 0:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        low, high = low + 1, high - 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    elif distance > 0:
                        high -= 1
                    else:
                        low += 1
        return res