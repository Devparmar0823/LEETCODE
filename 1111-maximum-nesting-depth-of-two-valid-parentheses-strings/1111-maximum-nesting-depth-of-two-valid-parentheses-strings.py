class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Increment depth for an opening parenthesis
                depth += 1
                # Distribute based on depth parity (0 or 1)
                answer.append(depth % 2)
            else:
                # Distribute based on depth parity before decrementing
                answer.append(depth % 2)
                # Decrement depth for a closing parenthesis
                depth -= 1
                
        return answer
