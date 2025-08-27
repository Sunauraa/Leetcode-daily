class Solution:
    def numTeams(self, rating: List[int]) -> int:
        segs = SortedList()
        n = len(rating)
        ans = 0
        for j in range(n):
            for k in range(j+1,n):
                if rating[k] > rating[j]:
                    ans+=segs.bisect_right(rating[j]-1)
                elif rating[k] < rating[j]:
                    ans+= len(segs) - segs.bisect_right(rating[j])
            segs.add(rating[j])
        return ans
