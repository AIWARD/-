UserName = input("请输入用户名")
PassWord = input("请输入密码")
if UserName == "seven" and PassWord == "123" :
    print("登陆成功")
else:
    print("登陆失败")

i = 2
sum = 0
while i in range(100):
    while i/2==0:
        sum+=i
    else:
        sum-=i
    i=i+1
print(sum)