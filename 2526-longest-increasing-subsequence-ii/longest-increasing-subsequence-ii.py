class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)
        #print(len(nums))
        arr = [0]*(n+2)
        segs = [0]*(4*n+3)
        ans = 0
        def update(id,l,r,key):
            if l > key or r < key:
                return
            if l == r:
                segs[id] = arr[l]
                return
            mid = (l+r)//2
            update(id*2,l,mid,key)
            update(id*2+1,mid+1,r,key)
            segs[id] = max(segs[id*2], segs[id*2+1])
    
        def take(id,l,r,u,v):
            if l > v or r < u:
                return 0
            elif l >= u and r <= v:
                return segs[id]
            mid = (l+r)//2
            return max( take(id*2,l,mid,u,v), take(id*2+1,mid+1,r,u,v) )
            
        for num in nums:
            mx = take( 1,1,n, num - k, num - 1 )
            #print(num)
            arr[num] = mx + 1
            ans = max(ans,arr[num])
            update(1,1,n, num)
        return ans
        