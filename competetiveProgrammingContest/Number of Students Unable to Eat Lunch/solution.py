class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length=len(students)
        while length:
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                length=len(students)
            else:
                students.append(students.pop(0))
                length-=1
        return len(students)