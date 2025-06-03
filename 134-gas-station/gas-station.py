class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        delta = [0]*n
        for i in range(n):
            delta[i] = gas[i] - cost[i]
        sumleft = [delta[0]]*n
        for i in range(1, n ):
            sumleft[i] = sumleft[i-1] + delta[i]
        minleft = [sumleft[0]]*n
        for i in range(1,n):
            minleft[i] = min(minleft[i-1], sumleft[i])
        minright = [sumleft[n-1]]*n
        for i in range(n - 2 , -1 , -1 ):
            minright[i] = min( minright[i+1] , minleft[i] )
        print(delta,sumleft,minleft,minright)
        for i in range(n):
            if i == 0:
                if minleft[n-1] >= 0:
                    return i
            else:
                if minright[i] - sumleft[i-1] >= 0 and sumleft[n-1] - sumleft[i-1] >= -minleft[i]:
                    return i
        return -1