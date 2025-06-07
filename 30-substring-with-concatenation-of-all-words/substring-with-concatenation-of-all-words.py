class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        step = len(words)*len(words[0])
        ans = []
        m = defaultdict(int)
        for i in words:
            m[i]+=1
        for i in range(n-step + 1):
            temp = s[i:i+step]
            mi = m.copy()
            if self.check(temp,words,mi):
                ans.append(i)
        return ans
    def check(self,s,words,m):
        n = len(words)
        step = len(s)//n
        for i in range(0 , len(s) , step ):
            if not m[s[i:i+step]]:
                return False
            else:
                m[s[i:i+step]] -=1
        return True

        