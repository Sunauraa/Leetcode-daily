class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        cur = n+1

        def check( cur ):
            m = defaultdict(int)
            while cur > 0:
                m[cur%10]+=1
                cur//=10
            for i in m.keys():
                if i != m[i]:
                    return False
            return True

        while not check(cur):
            cur+=1
        return cur