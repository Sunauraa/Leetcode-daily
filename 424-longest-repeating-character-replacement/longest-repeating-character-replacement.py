class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for o in range(26):
            char = chr(ord('A') + o)
            cnt = k
            j = 0
            for i in range(n):
                while j < n and (s[j] == char or cnt > 0):
                    if s[j]!=char:
                        cnt-=1
                    j+=1
                #print(i,j)
                ans = max(ans,j-i)
                if s[i]!= char:
                    cnt+=1
            #print()
        return ans