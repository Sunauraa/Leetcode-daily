class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(grid)
        for i in range(n-1, -n, -1):
            j = 0
            while i < 0:
                i+=1
                j+=1
            temp = SortedList()
            while i < n and j < n:
                temp.add(grid[i][j])
                i+=1
                j+=1
            if j == n and i != n:
                ans.append(temp[::])
            else:
                ans.append(temp[::-1])
        #print(ans)
        res = []
        for i in range(n-1,-1,-1):
            temp = []
            #print(ans)
            for j in range(i,i+n):
                temp.append(ans[j][0])
                ans[j] = ans[j][1:]
            res.append(temp)
        return  res
