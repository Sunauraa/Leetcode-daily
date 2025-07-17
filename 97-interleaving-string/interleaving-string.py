class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        check = False
        store = set()
        def dfs(x,y,z):
            nonlocal check
            #print(x,y,z)
            if not x and not y and not z:
                check = True
                return
            if not x and y == z:
                check = True
                return
            if not y and x == z:
                check = True
                return
            if not x or not y or not z:
                return
            if x[0] == z[0] and not check:
                temp1 = x[1:]
                temp2 = z[1:]
                p = tuple((temp1,y,temp2))
                if p not in store:
                    store.add(p)
                    dfs( temp1, y, temp2 )
            if y[0] == z[0] and not check:
                temp1 = y[1:]
                temp2 = z[1:]
                p = tuple((temp1,y,temp2))
                if p not in store:
                    store.add(p)
                    dfs( x, temp1, temp2 )
        dfs(s1,s2,s3)
        return check