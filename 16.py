import module
x = input("请输入操作数")
z = input("请输入操作符（+，-，×，/）")
y = input("请输入被操作数")
try:
    x = int(x)
    y = int(y)
except ValueError:
    print("数字输入错误")
if z == "+" :
    print(x,z,y,"=",module.addtion(x,y))
elif z == "-" :
    print(x,z,y,"=",module.subtraction(x,y))
elif z == "*" :
    print(x,z,y,"=",module.multiplication(z,y))
elif z == "/" :
    print(x,z,y,"=",module.division(x,y))
else:
    print("输入有误")