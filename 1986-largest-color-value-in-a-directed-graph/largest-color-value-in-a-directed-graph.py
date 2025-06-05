class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        color_count = [ [0]*26 for i in range(n) ]
        indegree = [0]*n

        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        q = deque( i for i in range(n) if indegree[i] == 0 )
        

        processed = 0
        max_value = 0
        while q:
            node = q.popleft()
            processed +=1
            cur_color = ord( colors[node] ) - ord('a')
            color_count[node][cur_color]+=1
            max_value = max(max_value, color_count[node][cur_color])
            for v in graph[node]:
                for c in range(26):
                    color_count[v][c] = max(color_count[v][c], color_count[node][c])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)


        return max_value if processed == n else -1

