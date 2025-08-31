class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        segs = [0]*(4*n+5)

        def minVal( x,y ):
            if x == -1:
                return y
            if y == -1:
                return x
            #print(x,y)
            if heights[x] >= heights[y]:
                return y
            else:
                return x

        def build(id,l,r):
            if l == r:
                segs[id] = l
                return
            mid = (l+r)//2
            build(id*2, l, mid)
            build(id*2+1, mid+1, r)
            segs[id] = minVal( segs[id*2], segs[id*2+1])

        #@cache
        def take(id, l, r, u, v):
            if l > v or r < u:
                return -1
            
            if l >= u and r <= v:
                return segs[id]
            mid = (l+r)//2
            return minVal( take(id*2,l,mid,u,v),take(id*2+1,mid+1,r,u,v) )

        
        ans = 0
        def sol(left,right):
            nonlocal ans
            idx = take(1,0,n-1,left,right)
            ans = max(ans,heights[idx]*(right-left+1))
            if idx-1 >= left:
                sol(left,idx-1)
            if idx + 1 <= right:
                sol(idx+1,right)


        build(1,0,n-1)
        sol(0,n-1)
        return ans
            

                


        