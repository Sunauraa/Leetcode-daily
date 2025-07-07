class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        m = defaultdict(list)

        for u,v in prerequisites:
            indegree[u]+=1
            m[v].append(u)

        queue = deque()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)

        #print(indegree)
        ans = []
        while queue:
            u = queue.popleft()
            ans.append(u)

            for v in m[u]:
                indegree[v]-=1
                if indegree[v] == 0:
                    queue.append(v)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []