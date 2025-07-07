class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        n = numCourses
        indegree = [0]*numCourses
        ans = []

        for u,v in prerequisites:
            m[v].append(u)
            indegree[u] +=1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        ans = 0

        while queue:
            u = queue.popleft()
            ans +=1

            for v in m[u]:
                indegree[v] -=1
                if indegree[v] == 0:
                    queue.append(v)

        return ans == n