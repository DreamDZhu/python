import os
import sys


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core import school

# 创建两所学校
ob_bj = school.School('光明学院', '北京')
ob_sh = school.School('黑暗学院', '上海')

# 来点老师
ob_sh.enroll_teacher()

# 创建三个课程
ob_bj.create_subject('linux 云计算', "6个月", "12800")
ob_bj.create_subject('python 全栈', "6个月", "18800")
ob_sh.create_subject('golang 后端开发', "4个月", "8800")

# 创建班级



