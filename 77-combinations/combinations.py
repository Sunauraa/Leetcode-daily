class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        store = set()
        def dequy( arr, index, cur ):
            for i in range( cur, n+1):
                nx = arr.copy()
                nx.append(i)
                #print(nx,index)
                if index == k:
                    ans.append(nx)
                else:
                    dequy(nx, index + 1, i + 1)
        
        dequy( [] , 1,1)
        return list(ans)

