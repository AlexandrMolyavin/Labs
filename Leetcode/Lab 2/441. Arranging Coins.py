class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        while n > 0:
            k+=1
            n -= k
        return k-1
