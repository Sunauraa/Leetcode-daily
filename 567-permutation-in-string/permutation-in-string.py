class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = defaultdict(int)
        for num in s1:
            m[num]+=1
        j = 0
        le = len(s1)
        s1 = set(s1)
        cnt = 0
        n= len(s2)
        for i in range(n):
            if j < i:
                j = i
                cnt = 0
            while j < n and m[s2[j]]:
                m[s2[j]]-=1
                j+=1
                cnt+=1
            print(cnt)
            if cnt == le:
                return True
            if s2[i] in s1:
                m[s2[i]]+=1
                cnt-=1
        return False