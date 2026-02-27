class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n,3)
        dp = [ [0]*( (1 << n)) for _ in range(presses + 1) ]
        dp[0][0] = 1
        for i in range(1,presses + 1):
            #print("presses:", i)
            for state in range( (1 << (n)) ):
                # button 1:
                prevstate = state
                for j in range(0,n):
                    prevstate^=(1<<j)
                if dp[i-1][prevstate]:
                    dp[i][state] = 1
                # button 2:
                prevstate = state
                for j in range(1,n,2):
                    prevstate^=(1<<j)
                if dp[i-1][prevstate]:
                    dp[i][state] = 1
                # button 3:
                prevstate = state
                for j in range(0,n,2):
                    prevstate^=(1<<j)
                if dp[i-1][prevstate]:
                    dp[i][state] = 1
                # button 4:
                prevstate = state
                for j in range(0,n,3):
                    prevstate^=(1<<j)
                if dp[i-1][prevstate]:
                    dp[i][state] = 1
                #print(bin(state), dp[i][state])
        #print()
        #print(dp[presses])
        return sum(dp[presses])