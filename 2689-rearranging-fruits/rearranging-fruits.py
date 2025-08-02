class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        m = defaultdict(int)
        mn1 = min(basket1)
        mn2 = min(basket2)
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for x,y in zip(basket1,basket2):
            m[x]+=1
            m[y]+=1
            m1[x]+=1
            m2[y]+=1
        if any(x%2 for x in m.values()):
            return -1
        store = SortedList()
        for x in m1.keys():
            if m1[x] > m2[x]:
                temp = min(x,mn1*2,mn2*2)
                for _ in range((m1[x] - m2[x])//2):
                    store.add(temp)
        for x in m2.keys():
            if m2[x] > m1[x]:
                temp = min(x,mn1*2,mn2*2)
                for _ in range((m2[x] - m1[x])//2):
                    store.add(temp)

        return sum(store[:(len(store)//2)])
        