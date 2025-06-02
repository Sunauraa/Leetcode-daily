class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        i = 1
        prev = 1
        ans = 0
        while i < n:
            if ratings[i] > ratings[i-1]:
                if i == 1:
                    ans+=prev
                prev +=1
                ans += prev
            elif ratings[i] == ratings[i-1]:
                if i == 1:
                    ans += 1
                prev = 1
                ans += prev
            else:
                j = i- 1
                while j < n - 1 and ratings[j] > ratings[j+1]:
                    j+=1
                dis = j - i + 2
                if dis > prev:
                    if i-1 != 0:
                        ans-=prev
                    ans+= (dis)*(dis+1)//2
                    prev = 1
                else:
                    dis-=1
                    ans+= dis*(dis+1)//2
                    prev = 1
                i = j
            i+=1
        return ans
                        

                

        