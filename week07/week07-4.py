##week07-4.py leetcode 394
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        n,ss=0,''
        for c in s:
            if c.isdigit():
                n=n*10+int(c)
            elif c.isalpha():
                ss+=c
            elif c=='[':
                stack.append((n,ss))
                ss,n='',0
            elif c==']':
                pn,ps=stack.pop()
                ss=ps+pn*ss
        return ss
