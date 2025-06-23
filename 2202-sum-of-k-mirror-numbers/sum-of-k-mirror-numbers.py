class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def createPalindrome(num,odd):
            x = num
            if odd:
                x//=10
            while x > 0:
                num = num*10 + x%10
                x//=10
            return num
        
        def isPalindrome(num,base):
            digits = []
            while num > 0:
                digits.append(num%base)
                num//=base
            return digits == digits[::-1]
        ans = 0
        length = 1
        while n > 0:
            for i in range(length, length*10):
                if n <= 0:
                    break
                p = createPalindrome(i,True)
                if isPalindrome(p,k):
                    ans+=p
                    n-=1
            for i in range(length, length*10):
                if n <= 0:
                    break
                p = createPalindrome(i,False)
                if isPalindrome(p,k):
                    ans+=p
                    n-=1
            length*=10   
        return ans             
