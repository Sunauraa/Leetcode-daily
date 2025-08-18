class Solution:
    def judgePoint24(self, a: List[int]) -> bool:
        if len(a)==1: return isclose(a[0],24)
        return any(self.judgePoint24([q]+rest)
            for v,u,*rest in permutations(a)
                for q in {v+u,v-u,v*u,u and v/u})