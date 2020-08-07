# Sorting bootcamp
class Student(object):
    def __init__(self, name, grade_point_average):
        self.name = name
        self.grade_point_average = grade_point_average

    def __lt__(self, other):
        return self.name < other.name


students = [
    Student('A', 4.0),
    Student('B', 3.0),
    Student('C', 2.0),
    Student('D', 3.2)
]

# sort by name
students_sort_by_name = sorted(students)
# sort by gpa
students.sort(key=lambda student: student.grade_point_average)

# Compute the intersection of two sorted arrays
def intersect_two_sorted_array(A, B):
    i, j, intersection_of_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            intersection_of_A_B.append(A[i])
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_of_A_B


