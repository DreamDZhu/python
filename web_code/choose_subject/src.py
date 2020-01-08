__author__ = "Ddz"
# 学校


class School:
    # 开设课程列表
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []  # 学员
        self.staffs = []  # 员工
        self.subjects = []  # 课程

    def enroll(self, stu_obj):
        print("为学员%s 办理注册手续", stu_obj.name)
        self.students.append(stu_obj)

    def create_subject(self, name, time, price):
        self.subjects.append(Subject(name, time, print()))

    def create_class(self):
        pass


# 课程
class Subject:
    def __init__(self, name, time, price):
        self.c_name = name
        self.c_time = time
        self.c_price = price


# 班级
class Clas:
    def __init__(self):
        pass


#讲师
class Teacher:
    def __init__(self):
        pass


# 学生
class Student:
    def __init__(self):
        pass

# bj_school = School("python")
# bj_school.create_subject("linux","6个月",12800)
#
# print(bj_school.subject_lst['linux'].c_price)

# linux = Subject("linux", "6个月", 12800)
# python = Subject("python", "6个月", 18800)
# go = Subject("go", "4个月", 8800)
