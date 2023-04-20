class teacher:

    '作为基础类测试'
    num=0
    def tea(self):
        print('必备技能')
        num1=1
print(teacher().__doc__)
del teacher.num
t=teacher()
t.agem=3
#print(teacher().num)
teacher.age=2
# print(teacher().agem)
print(t.agem)
