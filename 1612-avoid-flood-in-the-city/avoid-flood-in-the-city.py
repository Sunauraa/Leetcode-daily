class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        candry = SortedList()
        m = defaultdict(int)
        n = len(rains)
        res = [-1]*n
        for i,x in enumerate(rains):
            #print(i,x,m[x])
            if x == 0:
                candry.add(i+1)
            else:
                if m[x] == 0:
                    m[x] = i+1
                    res[i] = -1
                else:
                    if candry:
                        pos = candry.bisect_left(m[x])
                        if pos == len(candry):
                            return [] 
                        j = candry[pos]
                        candry.remove(j)
                        res[j-1] = x
                        m[x] = i+1
                    else:
                        return []
            #print(m[x])
            #print()
        while candry:
            pos = candry.pop()
            res[pos-1] = 1
        return res
