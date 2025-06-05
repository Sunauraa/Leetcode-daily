class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        curline = 0
        ans = []
        i = 0
        while i < n:
            backpack = maxWidth
            j = i
            while j < n and backpack - len(words[j]) - (j - i) >= 0:
                backpack-= len(words[j])
                j+=1
            temp = ''
            left = backpack
            numspace = j - i - 1
            if numspace !=0:
                minspace = left//numspace
            print(left,numspace)
            if j != n:
                for o in range( i , j ):
                    temp+=words[o]
                    if numspace == 0:
                        temp+=(' '*left)
                        break
                    if o == j -1:
                        continue
                    if left%(numspace):
                        temp+=(' '*(minspace+1))
                        left -= (minspace + 1)
                        numspace-=1
                    else:
                        temp+=(' '*(minspace))
                        left -= minspace
                        numspace-=1
            else:
                for o in range(i , j):
                    temp += words[o]
                    if left > 0:
                        temp += ' '
                        left-=1
                temp+= ' '*left
            ans.append(temp)
            i = j
        return ans

            


        