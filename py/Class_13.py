class Student:
    def __init__(self, name, job="无", time=0.00, time_effective=0.00): 
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective

    def count_time(self, hour, rate=0.8):
        self.time += hour
        self.time_effective += hour * rate

    def print_result(self):
        print('''
        学生: {}
        工作: {}
        时间: {}
        有效时间: {}
        '''.format(self.name, self.job, self.time, self.time_effective))
# 请你完成子类的定制（包括初始化方法和count_time函数）
class Programmer(Student):
    def __init__(self, name, job="Programmer", time=0.00, time_effective=0.00):
        Student.__init__(self, name, job, time, time_effective)

    def count_time(self, hour, rate=1.0):
        Student.count_time(self, hour, rate)

# 通过两个实例，完成子类和父类的对比（可自行验证）
student1 = Student('韩梅梅')
student2 = Programmer('李雷')

student1.count_time(8)
student2.count_time(8)

student1.print_result()
student2.print_result()