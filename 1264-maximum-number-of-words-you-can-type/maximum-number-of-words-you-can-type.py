class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = 0
        text = text.split()
        for w in text:
            wow = True
            for i in w:
                if i in brokenLetters:
                    wow = False
                    break
            cnt+= wow
        return cnt