# Student 클래스를 만들고
# name, id, courses


class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = []      #리스트로 만들기


#수강신청하는
    def enroll(self, course):
        self.courses.append(course)

#과목만들기

class Course:

    def __init__(self, name, code, capacity):
        self.name = name
        self.code = code
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        else:
            print(f'{student}님 인원이 꽉차서 수강신청이 불가합니다.')
            return False
class Registrar:
    def __init__(self):
        self.students = []
        self.courses = []

    def resister_course(self, student, course):
        res = course.add_student(student)
        if res:
            student.enroll(course)
        else:
            pass


