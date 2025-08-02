class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        m = defaultdict(int)
        for x,y in zip(basket1,basket2):
            m[x]+=1
            m[y]+=1
        for x in m.values():
            if x%2:
                return -1
        
        mn1 = min(basket1)
        mn2 = min(basket2)
        ans = 0
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for x,y in zip(basket1,basket2):
            m1[x]+=1
            m2[y]+=1
        store = SortedList()
        for x in m1.keys():
            if m1[x] > m2[x]:
                for _ in range((m1[x] - m2[x])//2):
                    store.add(min(x,mn1*2,mn2*2))
        #print(m1.keys())
        for x in m2.keys():
            if m2[x] > m1[x]:
                for _ in range((m2[x] - m1[x])//2):
                    store.add(min(x,mn1*2,mn2*2))

        #print(store)
        return sum(store[:(len(store)//2)])
        