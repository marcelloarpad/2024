class Student:
    def __init__(self, name, age, xingbie):
        self.name = name
        self.age = age
        self.xingbie = xingbie

    def study(self, kemu_name):
        print(f'{self.name}, {self.age}, {self.xingbie}正在学习{kemu_name}')

    def play(self, game_name):
        print(f'{self.name}, {self.age}, {self.xingbie}正在玩{game_name}')
    def __repr__(self):
        return f'{self.name}, {self.age}, {self.xingbie}'
stu1 = Student("XIAOM", "15", "N")
stu2 = Student("XIAOH", "16", "V")
print(stu1)
print(stu2)
stu1.study("python")
stu2.play("lanqiu")