class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        mi = defaultdict(int)
        for i in t:
            mi[i]+=1
        j = 0
        count = len(mi.keys())
        curlen = n + 1
        ans = ''
        for i in range(n):
            while j < n and count > 0:
                if s[j] in t:
                    mi[s[j]]-=1
                    if mi[s[j]] == 0:
                        count -=1
                j+=1
            #print(count,i,j, count == 0, curlen, j-i)
            if count == 0 and curlen > j - i:
                curlen = j - i
                ans = s[i:j]
                #print(ans)
            if s[i] in t:
                mi[s[i]]+=1
                if mi[s[i]] == 1:
                    count+=1
        return ans
        