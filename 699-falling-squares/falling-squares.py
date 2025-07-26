class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        cur = []
        m = defaultdict(int)
        mx = 0
        for i in range(len(positions)):
            l = positions[i][0]
            r = l + positions[i][1]
            height = 0
            for a,b in cur:
                if l < b and r > a:
                    height = max(height, m[(a,b)])
            #print(height)
            mx = max(mx,height + positions[i][1])
            m[(l,r)] = height + positions[i][1]
            ans.append(mx)
            cur.append([l,r])
        return ans
