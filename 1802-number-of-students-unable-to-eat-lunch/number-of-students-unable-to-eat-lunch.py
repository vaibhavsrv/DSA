class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        j = 0
        while students and j < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                j = 0

            else:
                students.append(students.pop(0))
                j+=1
        return len(students)