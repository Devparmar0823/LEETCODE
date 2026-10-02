class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        s=0
        if coordinates[0]=="a":
            s+=1
        elif coordinates[0]=="b":
            s+=2
        elif coordinates[0]=="c":
            s+=3
        elif coordinates[0]=="d":
            s+=4
        elif coordinates[0]=="e":
            s+=5
        elif coordinates[0]=="f":
            s+=6
        elif coordinates[0]=="g":
            s+=7
        elif coordinates[0]=="h":
            s+=8
        
        s+=int(coordinates[1])
        if s%2==0:
            return False
        return True