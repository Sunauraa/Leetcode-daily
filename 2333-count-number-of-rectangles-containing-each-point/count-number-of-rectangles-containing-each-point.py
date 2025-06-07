class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        area = defaultdict(list)
        for l,h in rectangles:
            for i in range(h+1):
                area[i].append(l)
        for x in area.keys():
            area[x].sort()
        ans = []
        for u,v in points:
            ans.append(self.binsearch(area[v], u))
        return ans
    def binsearch(self, arr , x ):
        #print(arr , x)
        l = 0
        n = len(arr)
        r = len(arr) - 1
        ans = 0
        #print(l,r)
        while l <= r:
            mid = (l+r)//2
            if arr[mid] >= x:
                r = mid -1
                ans = n - mid
            else:
                l = mid + 1
            #print(ans)
        #print()
        return ans

        