class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        ans = 0
        for pas,tot in classes:
            if pas == tot:
                ans+=1
            else:
                heapq.heappush(q, ( -((pas+1)/(tot+1) - pas/tot), pas/tot, pas , tot ))
        
        while q and extraStudents:
            extraStudents-=1
            _, rat, pas,tot = q[0]
            heapq.heappop(q)
            pas+=1
            tot+=1
            heapq.heappush(q, ( -((pas+1)/(tot+1) - pas/tot), pas/tot, pas , tot ))
            #print(q)
        
        #print(q)
        for incre,rat,tot,pas in q:
            ans+=rat
        return ans/(len(classes))