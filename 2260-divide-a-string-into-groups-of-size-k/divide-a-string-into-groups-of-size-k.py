class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        n = len(s)
        for i in range(0,n,k):
            if i + k < n:
                ans.append(s[i:i+k])
            else:
                ans.append(s[i:]+fill*(k-(n-i)))
        return ans