class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        operator = ['+','-','(',')']
        close = deque()
        stack = []
        cur = 0
        def calc(start):
            res = int(stack[start+1])
            #print(stack[:start])
            for i in range(start + 1 , len(stack) - 1, 2):
                op = stack[i+1]
                num2 = int(stack[i+2])
                #print(res,op,num2)
                if op == '-':
                    res = res - num2
                else:
                    res = res + num2
                #print(res)
                
            return str(res)
        for i in range(n):
            if s[i] == ' ':
                continue
            elif s[i] == '(':
                close.append(len(stack))
                stack.append(s[i])
            elif s[i] == ')':
                start = close.pop()
                if stack[start+1] == '-':
                    stack[start+2] = str((-1)*int(stack[start+2]))
                    res = calc(start+1)
                #print(start, stack)
                else:
                    res = calc(start)
                stack = stack[:start]
                stack.append(res)
            elif s[i] in ['+','-']:
                stack.append(s[i])
            else:
                if stack and stack[-1] not in ['-','+','(',')']:
                    stack[-1] = stack[-1] + s[i]
                else:
                    if stack and stack[-1] == '-':
                        if len(stack) > 1 and stack[-2] != '(':
                            stack[-1] = '+'
                            stack.append('-'+s[i])
                        else:
                            stack[-1] = ('-' + s[i])
                    else:
                        stack.append(s[i])
            #print(stack)
            i+=1
        #print(stack)
        if stack[0] == '-':
            stack[1] = str((-1)*int(stack[1]))
            return int(calc(0))
        return int(calc(-1))

                    

            