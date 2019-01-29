class animals:
    def __init__(self, cate,colo):
        self.cate = cate  #定义种类
        self.colo = colo  #定义颜色
        print("\nThis is a",self.cate,", the color is ",self.colo,end='')

    def run(self):
        print("\nThe {cate} of {color} are running".format(cate=self.cate,color=self.colo),end='')
    
    def eat(self):
        print("\nThe {cate} of {color} are eating".format(cate=self.cate,color=self.colo),end='')
tiger = animals("tiger","yellow")
tiger.eat()
tiger.run()

class cock(animals):
    def __init__(self, cate, colo,name):
        animals.__init__(self, cate, colo)
        self.name = name
        print(" and this name is ",self.name)
    
    def run(self):
        animals.run(self)
        print(" and this name is ",self.name)

    def eat(self):
        animals.eat(self)
        print(" and this name is ",self.name)
cock1 = cock("cock","red","jack")
cock1.eat()
cock1.run()