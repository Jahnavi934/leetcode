class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMapForMagazine = defaultdict(int)
        for i in magazine:
            hashMapForMagazine[i] = hashMapForMagazine[i] + 1
        for i in ransomNote:
            if i in hashMapForMagazine and hashMapForMagazine[i] != 0:
                hashMapForMagazine[i] = hashMapForMagazine[i] - 1
            else:
                return False
        return True