# 组合
# 一个类的对象是另外一个类对象的属性


class Student:
    def __init__(self, name, age, sex, classid, phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.classid = classid
        self.phone = phone


class Clas:
    def __init__(self, cname, begint, teacher):
        self.cname = cname
        self.begint = begint
        self.teacher = teacher


py22 = Clas('22期', '2019.08.10', '教师A')
py23 = Clas('23期', '2019.09.22', '教师B')

# 组合 ，将对象py22 ，直接作为classid 传递给 大壮这个对象
大壮 = Student('大壮', 18, 'male', py22, '13888888888')
小白 = Student('小白', 22, 'male', py23, '13999999999')

print(大壮.classid.begint)  # 将相关的对象组合到一起，直接调用
print(小白.classid.begint)


# 班级类
# 包含一个属性，课程

# 课程
# 课程名称
# 课程周期
# 价格3

# 创建两个班级 linux57 与 Python 22 ，查看linux57所学课程的价格 ，py22期所学课程的周期

class room:
    def __init__(self, course):
        self.course = course


class Course:
    def __init__(self, name, time, price):
        self.name = name
        self.time = time
        self.price = price

linux = Course('linux云计算架构','6个月','12800')
python = Course('python全栈开发','6个月','18800')

linux_57 = room(linux)
python_22 = room(python)

print(linux_57.course.price)
print(python_22.course.time)

# 在创建多个对象的时候，组合会让我们可以合并多个重复元素