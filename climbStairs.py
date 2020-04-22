class Solution:
    def climbStairs(self, n):
        result=[]

        result.append(0)
        result.append(1)
        result.append(2)
        for i in range(3, n+1):
            r= result[n-1]+ result[n-2]
            result.append(r)
        return result 


















