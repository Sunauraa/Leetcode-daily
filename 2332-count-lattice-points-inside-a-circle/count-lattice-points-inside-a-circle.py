class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        for u in range(201):
            for v in range(201):
                check = 0
                for x,y,r in circles:
                    if ( u - x )**2 + (v-y)**2 <= r**2:
                        check = 1
                        break
                if check:
                    ans+=1
        return ans