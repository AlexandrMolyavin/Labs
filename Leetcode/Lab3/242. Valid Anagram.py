class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for item in s:
           if item in t:
                s = s[:s.index(item)] + s[s.index(item) + 1:]
                t = t[:t.index(item)] + t[t.index(item) + 1:]

        return True if len(s) == 0 else False