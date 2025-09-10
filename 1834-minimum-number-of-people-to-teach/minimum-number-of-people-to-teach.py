class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        res = inf
        store = []
        added = []
        for u,v in friendships:
            if not any(x in languages[u-1] for x in languages[v-1] ):
                if u-1 not in added:
                    store.append(languages[u-1])
                    added.append(u-1)
                if v - 1 not in added:
                    store.append(languages[v-1])
                    added.append(v-1)
        for i in range(1,501):
            res = min(res, sum([ i not in x for x in store ]) )
        return res