class Solution:
    def sortVowels(self, s: str) -> str:
        ans = []
        store = SortedList()
        pos = []
        vowel = 'AEIOUaeiou'
        for i,char in enumerate(s):
            ans.append(0)
            if char in vowel:
                pos.append(i)
                store.add( ord(char) )
            else:
                ans[i] = char
    
        for i,p in enumerate(pos):
            ans[p] = chr(store[i])

        #print(ans)
        return ''.join(ans)
                

        