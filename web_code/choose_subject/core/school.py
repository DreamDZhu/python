from . import subject
from . import classes
from . import student
from . import teacher


class School:
    # 开设课程列表
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []  # 学员
        self.teacher = []  # 员工
        self.subjects = []  # 课程
        self.classes = []  # 班级

    # 创建课程
    def create_subject(self, name, time, price):
        course = subject.Subject(name, time, price)
        self.subjects.append(course)
        return course


    def

    def enroll_student(self, stu_obj):
        print("为学员%s 办理注册手续", stu_obj.name)
        self.students.append(stu_obj)

    def enroll_teacher(self, th_obj):
        print("为老师%s 办理注册手续", th_obj.name)
        self.teacher.append(th_obj)

    def create_class(self, subject, teacher):
        self.classes.append(subject, teacher)




