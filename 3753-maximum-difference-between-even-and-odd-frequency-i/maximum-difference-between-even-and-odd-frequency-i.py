class Solution:
    def maxDifference(self, s: str) -> int:
        m = defaultdict(int)
        minodd = 100
        mineve = 100
        maxodd = 0
        maxeve = 0
        for i in s:
            m[i] += 1
        for i in 'qwertyuiopasdfghjklzxcvbnm':
            if m[i]:
                if m[i]%2:
                    maxodd = max(maxodd, m[i])
                    minodd = min(minodd, m[i])
                else:
                    maxeve = max(maxeve, m[i])
                    mineve = min(mineve, m[i])
        return maxodd - mineve
        