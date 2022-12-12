class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        sums = 0

        for i in nums:
            sums += i

            if sums - k in hashmap:
                count += hashmap[sums - k] 
            if sums in hashmap:
                hashmap[sums] += 1
            else:
                hashmap[sums] = 1

        return count