#1
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=[]
        for i in range(len(heights)):
            l.append([heights[i],names[i]])
        l.sort(reverse=True)
        k=[]
        for i in l:
            k.append(i[1])
        return k
 
#2 Quick sort
def sorting(heights):
    if len(heights) <= 1:
            return heights
    left = []
    right = []
    center = []
    elem = heights[0][1]
    for item in heights:
        if item[1] < elem:
            left.append(item)
        elif item[1] > elem:
            right.append(item)
        else:
            center.append(item)

    return sorting(right) + center + sorting(left)
    
    
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
       
        new_array =[(n, h) for n, h in zip(names, heights)]
       
 
        res = sorting(new_array)
        
        return [ n for n, h in res]
