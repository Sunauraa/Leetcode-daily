class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mn = prices[0]
        left = [0]*n
        left[0] = float('-inf')
        for i in range(1,n):
            #print(prices[i],mn)
            left[i] = max(left[i-1], prices[i]-mn)
            mn = min(mn,prices[i])

        print()
        mx = prices[n-1]
        right = [0]*n
        right[n-1] = float('-inf')
        for i in range(n-2,-1,-1):
            #print(prices[i],mx)
            right[i] = max(right[i+1],mx - prices[i])
            mx = max(mx,prices[i])
        
        #print(left)
        #print(right)
        res = 0
        for i in range(n):
            if i == 0:
                res = max(res,right[i])
            elif i == n-1:
                res = max(res,left[i])
            else:
                res = max(res, left[i] + right[i])
        return res
