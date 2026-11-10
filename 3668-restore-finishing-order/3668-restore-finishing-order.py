class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        output=[]
        for o in order:
            if o in friends:
                output.append(o)
        return output