class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=len(people)
        people.sort()
        i=0
        j=l-1
        c=0
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            else:
                j-=1
            c+=1
        return c
   