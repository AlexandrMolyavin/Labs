class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a = []
        for i in range(1,2001):
            if i not in arr:
                a.append(i)
        return a[k-1]