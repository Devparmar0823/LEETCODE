class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i=0
        j=0
        for c in commands:
            if c=="RIGHT":
                j+=1
            elif c=="LEFT":
                j-=1
            elif c=="UP":
                i-=1
            else:
                i+=1
        return  (i*n)+j