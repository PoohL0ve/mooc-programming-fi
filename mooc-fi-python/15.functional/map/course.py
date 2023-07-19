class CourseAttempt :
    def __init__(self, name: str, course: str, grade: float) :
        self.name = name
        self.course = course
        self.__grade = grade

# Instances of the class
student1 = CourseAttempt('Bilal Song', 'Programming Fundamentals', 3.67)
student2 = CourseAttempt('Charles Olly', 'Business 101', 3.95)
student3 = CourseAttempt('Anna Burlington', 'Advance Economics', 3.87)

# list of students
students = [student1, student2, student3]

# using a map function to print names
who_did = list(map(lambda n: n.name, students))
for name in who_did :
    print(name)

# courses attempted in order
attempted_courses = list(map(lambda c: c.course, students))
attempted_courses.sort()
for course in attempted_courses :
    print(course)