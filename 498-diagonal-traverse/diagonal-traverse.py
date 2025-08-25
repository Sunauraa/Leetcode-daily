class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        store = []
        n,m = len(mat), len(mat[0])
        mx = n+m
        starti,startj = 0,0
        while starti != mx - 1:
            temp = []
            i,j = starti,0
            while i >= 0:
                if i < n and j < m:
                    temp.append(mat[i][j])
                i-=1
                j+=1
            store.append(temp)
            starti+=1
        ans = []
        check = True
        print(store)
        for arr in store:
            if not check:
                arr = arr[::-1]
            for num in arr:
                ans.append(num)
            check = not check
        return ans
