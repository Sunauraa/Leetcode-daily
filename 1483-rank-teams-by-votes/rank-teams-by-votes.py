class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes)
        m = defaultdict(list)
        for i in votes[0]:
            m[i] = [0]*26
        
        ans = list(votes[0])
        for num in votes:
            for i in range(len(num)):
                m[num[i]][i]+=1
        

        def comp( s1, s2 ):
            for i in range(26):
                if m[s1][i] > m[s2][i]:
                    return False
                elif m[s1][i] < m[s2][i]:
                    return True
            return ord(s1) > ord(s2)

        #print(ans)
        n = len(votes[0])
        for _ in range(n):
            for i in range(n-1):
                #print(i)
                if comp( ans[i], ans[i+1] ):
                    ans[i],ans[i+1] = ans[i+1],ans[i] 

        return ''.join(ans)
