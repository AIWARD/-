def sayhello():
    '''函数调用
    '''
    print("hello")

def printMax(a,b):
    '''函数形参
    '''
    if a > b :
        print(a,"is Maximum")
    else:
        print(b,"is Maximum")

f = "this is Global"
def func(f):
    '''局部变量
    '''
    f = "this is Area"
    print(f)

fc = "this is Global's fc"
def func2():
    '''访问外部变量
    '''
    global fc
    print("fc:",fc)
    fc = "this is Area's fc"
    print("fc(Changed):",fc)
    fc = "this is Global's fc"

def say(message,times = 1):
    '''默认参数
    '''
    print(message*times)

def func3(a,b=5,c=10):
    '''关键字传参
    '''
    print('a is', a, 'and b is', b, 'and c is', c)

def maximum(x,y):
    '''return
    ''' 
    if x > y :
        return x
    else :
        return y

def someFunction():
    pass 

def printMax2(x,y):
    '''Prints the maximum of two numbers.
 
    The two values must be integers.
    '''
    y = int(y)
    x = int(x)
    if x > y :
        print(x,"x is max")
    else:
        print(y,"y is max")

print(sayhello.__doc__)
sayhello()

print(printMax.__doc__)
printMax(10,20)

print(func.__doc__)
print(f)
func(f)

print(func2.__doc__)
func2()

print(say.__doc__)
say("hello\n",5)

print(func3.__doc__)
func3(3,7)
func3(25,c=24)
func3(c=50,a=100)

print(maximum.__doc__)
print("maximum(10,20):",maximum(10,20),"\n")

#print(someFunction().__doc__)
print(someFunction())

print(printMax2.__doc__)
printMax2(3,5)