class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        v = list(d.values())
        j,c = [],0
        for i in v:
            if i not in j:
                j.append(i)
            else:
                while i in j:
                    i -= 1
                    if i >= 0:
                        c += 1
                j.append(i)
        return c