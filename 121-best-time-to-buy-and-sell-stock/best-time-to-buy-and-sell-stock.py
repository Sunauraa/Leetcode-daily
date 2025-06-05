class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 10002
        mx = -1
        for i in prices:
            mn = min(mn,i)
            mx = max( mx , i - mn )
        return mx
        