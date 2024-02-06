class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        ana = {}
        for word in words:
            key = "".join(sorted(word))
            if key not in ana:
                ana[key] = [word]
            else:
                ana[key].append(word)
        return ana.values()