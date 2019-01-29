from decimal import *
import math
print("------------------------------------")
a = 0o101
b = 64
c = -237
d = 0x80
e = -0x92
print(str(a),str(b),str(c),str(d),str(e))

print("------------------------------------")
longint = 99999**9
print(str(longint))

print("------------------------------------")
print(bool(1))
print(bool(True))
print(bool('0'))
print(bool([]))
print(bool((1, )))

print("------------------------------------")
foo = 42
bar = foo<42
print(bar,bar+10)
print('%s' %bar)
print('%d' %bar)

print("------------------------------------")
class C :pass
c=C()
print(str(bool(c)))

print("------------------------------------")
print(0.0,-777.,-5.555555,96e3 * 1.0,-1.609e-19)

print("------------------------------------")
print(complex(2,4),1.23e-045+6.7e+089j)

print("------------------------------------")
dec = Decimal('.1')
print(dec),(Decimal(.1),dec + Decimal(.1))

print("------------------------------------")
print(int(4.1231),float(4),complex(4))

print("------------------------------------")
print(hex(255),oct(255),oct(0x111))

print("------------------------------------")
print(chr(76),ord('L'))

print("------------------------------------")
ceil_f = '''
ceil()函数作用为返回值上限的X,不小于x的最小整数。
个人理解：向无限大方向取最近的一位整数
例：math.ceil(40.12) == '''
print(ceil_f,math.ceil(40.12),"math.ceil(-40.12) ==",math.ceil(-40.12))

print("------------------------------------")
floor_f = '''
floor()函数作用为返回值下限的X,不大于于x的最大整数。
个人理解：向无限小方向取最近的一位整数
例：math.floor(40.12) == '''
print(floor_f,math.floor(40.12),"math.floor(-40.12) ==",math.floor(-40.12))

print("------------------------------------")
fabs_f = '''
fabs()作用为返回绝对值
例：math.fabs(40.12)'''
print(fabs_f,math.fabs(40.12),"math.fabs(-40.12)",math.fabs(-40.12))

print("------------------------------------")
factorial_f = '''
factorial()作用为求阶乘
例：factorial(10) =='''
print(factorial_f,math.factorial(10))

print("------------------------------------")
hypot_f = '''
hypot()作用为返回欧几里德范数 sqrt(x*x + y*y)
个人理解：对（平方和公式）的结果求平方根
math.hypot(10,12) =='''
print(hypot_f,math.hypot(10,12))

print("------------------------------------")
sqrt= '''
sqrt()作用为返回平方根
当sqrt(xx+yy）等价于hypot(x,y) 作用为返回欧几里德范数
例：math.sqrt(10*2+10*13) =='''
print(sqrt,math.sqrt(10*2+10*13))

print("------------------------------------")
