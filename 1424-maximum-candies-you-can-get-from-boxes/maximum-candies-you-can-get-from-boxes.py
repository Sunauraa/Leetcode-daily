class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(candies)
        q = deque()
        hadKeys = [0]*n
        hadBoxes = [0]*n
        ans = 0
        visit = [0]*n
        for u in initialBoxes:
            hadBoxes[u] +=1
        for u,v in enumerate(status):
            if v:
                hadKeys[u]+=1
                if hadBoxes[u] and hadKeys[u]:
                    q.append(u)
        while q:
            u = q.popleft()
            if visit[u]:
                continue
            visit[u] = 1
            ans+=candies[u]
            for v in containedBoxes[u]:
                hadBoxes[v]+=1
                if hadBoxes[v] and hadKeys[v]:
                    q.append(v)
            for v in keys[u]:
                hadKeys[v]+=1
                if hadBoxes[v] and hadKeys[v]:
                    q.append(v)
        return ans
