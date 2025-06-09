class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n,p,z = [], [], []
        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
            else:
                z.append(i)
        N,P = set(n) , set(p)
        if len(z) > 0:
            for i in p:
                if -i in n:
                    ans.append([ i , 0 , -i ])
            if len(z) > 2:
                ans.append([0,0,0])
        for i in range( len(p) - 1 ):
            for j in range( i + 1 , len(p) ):
                if -p[i]-p[j] in N:
                    ans.append( [ p[i] , p[j] , -p[i] - p[j] ] )
        for i in range( len(n) - 1 ):
            for j in range( i + 1 , len(n) ):
                if -n[i]-n[j] in P:
                    ans.append( [ n[i] , n[j] , -n[i] - n[j] ] )
        for x in ans:
            x.sort()
        ans.sort()
        if(len(ans) == 0):
            return []
        temp = [ans[0]]
        for x in ans[1::]:
            if(x == temp[-1]): continue
            temp.append(x)
        return temp