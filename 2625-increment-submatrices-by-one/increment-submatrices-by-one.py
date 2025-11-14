class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [ [0]*n for _ in range(n) ]
        for q,w,e,r in queries:
            for i in range(q,e+1):
                res[i][w]+=1
                if r < n - 1:
                    res[i][r+1]-=1
        #print(res)
        for i in range(n):
            for j in range(n):
                if j > 0:
                    res[i][j]+=res[i][j-1]
        return res