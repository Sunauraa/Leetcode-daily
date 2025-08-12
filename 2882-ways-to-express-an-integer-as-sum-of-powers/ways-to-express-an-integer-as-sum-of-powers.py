class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        arr = [0]*(n+1)
        arr[0] = 1
        MOD = 10**9+7
        for i in range(1,n+1):
            temp = i**x
            #print(i,temp)
            if temp > n:
                break
            for num in range(n,temp-1,-1):
                arr[num]+=arr[num-temp]
                arr[num]%=MOD
            #print(arr)
            #print()
        #print(arr)
        return arr[n]
