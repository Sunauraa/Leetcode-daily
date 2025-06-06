class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        m = dict()
        ans = 10**5 + 2
        for i,v in enumerate(cards):
            if v in m:
                ans = min(ans,i - m[v] + 1)
                m[v] = i
            else:
                m[v] = i
        if ans == 10**5 + 2:
            return -1
        else:
            return ans

        