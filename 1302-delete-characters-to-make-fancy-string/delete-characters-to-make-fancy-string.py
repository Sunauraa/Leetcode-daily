class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        #print(ans)
        for i in range(1, len(s)-1):
            #print(i,s[i],s[i-1],s[i-2])
            if s[i] != s[i-1] or s[i] != s[i+1]:
                #print(s[i])
                ans += s[i]
               # print(ans)
        if len(s) != 1:
            ans += s[-1]
        return ans