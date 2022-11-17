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