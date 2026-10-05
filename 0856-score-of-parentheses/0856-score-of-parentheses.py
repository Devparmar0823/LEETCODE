class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        stack=[0]
        for c in s:
            if c=="(":
                stack.append(0)
            else:
                score=stack.pop()
                stack[-1]+=max(2*score,1)
        return stack[0]