class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        m = defaultdict(int)
        line = []
        seg = []
        for l,r,h in buildings:
            line.append((l,-h,1))
            line.append((r,-h,0))
        line.sort()

        ans = []
        prevx = line[0][0]
        prevh = line[0][1]
        for l,h,tf in line:
            if l != prevx and( not ans or ans[-1][1] != prevh):
                ans.append([prevx,prevh])
            if tf:
                insort(seg, h)
            else:
                seg.remove(h)
            if seg:
                prevh = -seg[0]
            else:
                prevh = 0
            prevx = l
        ans.append([line[-1][0], 0])
        return ans
            