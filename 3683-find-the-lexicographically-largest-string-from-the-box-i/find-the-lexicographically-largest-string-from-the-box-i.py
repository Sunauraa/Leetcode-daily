class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        mx = max(word)
        n = len(word)
        if numFriends == 1:
            return word
        ans = ''
        for i in range(n):
            if word[i] == mx:
                j = n - numFriends + i + 1
                if j > i:
                    temp = word[i:j]
                    if ans < temp:
                        ans = temp
        return ans