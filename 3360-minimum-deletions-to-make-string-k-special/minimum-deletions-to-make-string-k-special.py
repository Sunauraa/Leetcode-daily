class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        m = defaultdict(int)
        for i in word:
            m[i]+=1
        mx = max(m.values())
        def check( line ):
            temp = 0
            for i in m.values():
                if i < line:
                    temp+=i
                else:
                    temp+= (i - (line + k))*(i-line > k)
            return temp
        ans = float('inf')
        for i in range(mx+1):
            ans = min(ans, check(i))
        return ans
        