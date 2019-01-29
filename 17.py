def hui(str):
    if str[::-1] == str :
        return True
    else:
        return False

while True:
    try :
        t = hui(input("请输入字符串"))
        if t == True:
            print("Yes")
            break
        else:
            raise ValueError
    except ValueError :
        print("请检查输入字符串是否为回文")