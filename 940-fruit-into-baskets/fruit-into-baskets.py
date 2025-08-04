class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dp = [ (-1,0) ]
        m = defaultdict(int)
        j = 0
        ans = 0
        cur = 0
        n = len(fruits)
        for i in range(len(fruits)):
            #print(i)
            while j < n and cur <= 2:
                m[fruits[j]]+=1
                if m[fruits[j]] == 1:
                    cur+=1
                j+=1
                #print(m)
            cmp = j - i
            if cur > 2:
                cmp-=1
            ans = max(ans,cmp)
            m[fruits[i]]-=1
            if m[fruits[i]] == 0:
                cur-=1
        return ans