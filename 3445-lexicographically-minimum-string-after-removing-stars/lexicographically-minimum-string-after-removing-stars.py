class Solution:
    def clearStars(self, s: str) -> str:
        m = defaultdict(list)
        n = len(s)
        print(n)
        res = ''
        letter = ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z').split(',')
        arr = [1]*n
        #print(arr)
        #print(m['d'])
        for i in range(n):
            if s[i] == '*':
                arr[i] = 0
                #print(arr)
                for j in letter:
                    if m[j]:
                        loc = m[j][len(m[j])-1]
                        arr[loc] = 0
                        m[j].pop()
                        break
            else:
                m[s[i]].append(i)
            #print(arr)
        for i in range(n):
            if arr[i]:
                res+=s[i]
        return res

                
        