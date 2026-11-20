class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        move=0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            move+=abs(seats[i]-students[i])
        return move