class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans = 0
        cur = ''
        for i in s:
            x  = 0
            y = 0
            temp = k
            count[i]+=1
            difx = abs(count['S'] - count['N'])
            minx = min(count['S'], count['N'])
            if temp > minx:
                x = difx + minx*2
                temp -= minx
            else:
                x = difx + temp*2
                temp -= temp
            dify = abs(count['E'] - count['W'])
            miny = min(count['W'], count['E'])
            if temp > miny:
                y = dify + miny*2
                temp -= miny
            else:
                y = dify + temp*2
                temp -= temp
            ans = max(ans,x+y)
        return ans
            