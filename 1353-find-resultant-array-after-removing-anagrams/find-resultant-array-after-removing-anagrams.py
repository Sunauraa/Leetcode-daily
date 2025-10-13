class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 0
        n = len(words)
        while i < n:
            #if i < n-1:
            #    print(i,sorted(words[i]), sorted(words[i+1]))
            if i < n - 1 and sorted(words[i]) == sorted(words[i+1]):
                words.remove(words[i+1])
                n-=1
            else:
                i+=1
        return words
