class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        a = {}
        for i in range(left,right+1):
            a[i] = False

        for item in a:
            for start,end in ranges:
                if start<=item<=end:
                    a[item] = True
                    break
            if a[item] == False:
                return False

        return True