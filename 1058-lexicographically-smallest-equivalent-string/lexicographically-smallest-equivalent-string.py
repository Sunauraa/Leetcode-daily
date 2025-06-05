class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        m = defaultdict(list)
        n = len(s1)
        for i in range(97, 123):
            m[i] = i
        for i in range(n):
            self.join_set( ord(s1[i]) , ord(s2[i]) , m )
        ans=''
        for i in range(len(baseStr)):
                ans += chr(self.parent(m,ord(baseStr[i])))
        return ans
    def parent(self , m , a):
        if a == m[a]:
            return a
        p = self.parent(m ,m[a])
        m[a] = p
        return m[a]
    def join_set(self, a , b , m ):
        a = self.parent(m,a)
        b = self.parent(m,b)
        if a > b:
            a,b = b,a
        m[b] = a
        return
    
            
        