class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        store = SortedList()
        cur = 1
        while cur < 10**9:
            store.add(cur)
            cur*=4
        #print(store)
        for l,r in queries:
            cur = r
            res = 0
            while cur >= l:
                idx = store.bisect_right(cur)
                #print(idx)
                res+= idx*(cur + 1 - max(store[idx-1],l))
                cur = max(store[idx-1],l) - 1
            #print(res)
            ans += res//2 + res%2
            #print()
        return ans


        return ans