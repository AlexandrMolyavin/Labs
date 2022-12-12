class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for word in strs:
            hcode = 1
            for letter in word:
                hcode *= hash(letter)
            if hcode in table:
                table[hcode].append(word)
            else:
                table[hcode] = [word]
        # putting each list of anagrams into a string
        results = []
        for key in table:
            results.append(table[key])
        return results