class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        store = SortedList()
        cnt = 0
        for i in range(n):
            if i == 0:
                store.add(neededTime[i])
                continue
            if colors[i] != colors[i-1]:
                if len(store) == 1:
                    store = SortedList()
                else:
                    cnt += sum(store[:-1])
                    store = SortedList()
            store.add(neededTime[i])
            #print(i,cnt,store)
        if len(store) > 1:
            cnt+= sum(store[:-1])
        return cnt