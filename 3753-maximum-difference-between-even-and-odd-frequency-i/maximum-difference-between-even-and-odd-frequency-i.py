class Solution:
    def maxDifference(self, s: str) -> int:
        m = defaultdict(int)
        minodd = 0
        mineve = 0
        maxodd = 100
        maxeve = 100
        for i in s:
            m[i] += 1
        for i in 'qwertyuiopasdfghjklzxcvbnm':
            if m[i]:
                if m[i]%2:
                    if minodd == 0:
                        minodd = i
                    if maxodd == 100:
                        maxodd == i
                    if m[i] < m[minodd]:
                        minodd = i
                    if m[i] > m[maxodd]:
                        maxodd = i
                        print('??')
                else:
                    if mineve == 0:
                        mineve = i
                    if maxeve == 100:
                        maxeve == i
                    if m[i] < m[mineve]:
                        mineve = i
                    if m[i] > m[maxeve]:
                        maxeve = i
        return m[maxodd]- m[mineve]
        