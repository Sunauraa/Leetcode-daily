class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort( key = lambda x: (-x[0],x[1]))
        ans = []
        for x in people:
            cnt = 0
            idx = 0
            n = len(ans)
            while cnt!= x[1] and idx < n:
                if ans[idx][0] >= x[0]:
                    cnt+=1
                idx+=1
            ans.insert(idx,x)
        return ans
