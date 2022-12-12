class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in hashmap:
                return [hashmap[delta],i]

            hashmap[nums[i]] = i