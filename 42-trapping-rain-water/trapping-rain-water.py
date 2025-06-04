class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxleft = [0]*(n+1)
        for i in range( n - 1 , -1 , -1 ):
            maxleft[i] = max(maxleft[i+1], height[i])
        ans = 0
        curheight = 0
        curwall = 0
        for i in range( n ):
            if curwall <= height[i]:
                curwall = min( height[i], maxleft[i+1] )
                continue
            if curwall > 0:
                ans+= curwall - height[i]
            print(ans,curwall)
        return ans

            