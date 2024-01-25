class Solution:
    def tribonacci(self, n: int) -> int:
        a1=0
        a2=1
        a3=1
        if n==0:
            return a1
        elif n==1 or n==2:
            return a2
        else:
            i=3
            while True:
                temp=a1+a2
                a1=a2
                a2=a3
                a3=a3+temp
                if i==n:
                    return a3
                i+=1
                