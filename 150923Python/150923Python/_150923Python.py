# 클래스 변수와 인스턴스 변수
# 인스턴스변수는 인스턴스를 만들어야 사용가능
# lastname : 클래스변수
# fullname : 인스턴스변수
# 내멤버만 신경쓰고 초기화시키면 된다
# 다른건 부모에 해당하는 생성자 호출하면 된다

#추상클래스는 객체를 만들수 없다. 
# 다중상속의 문제점 : 여러 클래스중에 중복되는 메소드가 있다면 
# c도 a를 상속받고 b도 a를 상속받으면 c가 b를 상속받을때 문제발생
# super : 중복되어도 부모에 해당하는걸 한번만 호출하게 해준다
#추상클래스 : 추상메소드를 포함하고있는 클래스
# 자식클래스는 반드시 추상메소드를 구현해야함
# 추상메소드 : 자식클래스에서 꼭 재정의되어야하는 메소드
#@abstractedmethod
# 다형성 : 다양한 객체들이 명령 하나로 다양하게 움직이는 것
# from abcimport ABCMeta, abstractedmethod


#class HousePark:
#    lastname = "박"
#    def __init__(self, name):
#        self.fullname = self.lastname + name
#    def travel(self, where):
#        print("%s, %s여행을 가다." % (self.fullname, where))
#class HouseKim(HousePark):
#    lastname = "김"
#    def __init__(self, name, age):
#        HousePark.__init__(self, name)
#        self.age = age
#    def travel(self, where, day):
#        HousePark.travel(self, where)
#        print("%s, %d살에 %s여행 %d일 가네." % (self.fullname, self.age, where, day))
#========================================================
#class A :
#    def __init__(self):
#        print("A 생성자 호출")
#class B(A) :
#    def __init__(self):
#        super().__init__()
#        print("B 생성자 호출")
#class C(A) :
#     def __init__(self):
#         super().__init__()
#         print("C 생성자 호출")
#class D(B,C):
#     def __init__(self):
#        super().__init__()
#        print("D 생성자 호출")
#===========================================================
#class Terran:
#    def __init__(self,name):
#        self.name=name

#class Tank(Terran):
#    def __init__(self,name,damage):
#        super().__init__(self,name)
#        self.damage=damage

#class Marine(Terran):
#    def __init__(self,name,hp):
#        super().__init__(self,name)
#        self.hp=hp

#t1=Tank("tank",0)
#t2=Marine("marine",100)
#print(t1)
## 테란 객체 자체는 없지만 탱크, 마린이라는 인스턴스가 존재(테란은 객체를 만드는 클래스가 아니라는 얘기
#=====================================

#from abc import ABCMeta, abstractmethod
#class Terran(metaclass=ABCMeta):
#    def __init__(self,name):
#        self.name=name
#    @abstractmethod
#    def attack(self):
#        pass

#class Tank(Terran):
#    def __init__(self,name,damage):
#        super().__init__(name)
#        self.damage=damage
#    def attack(self):
#        print("탱크를쏩니다")

#class Marine(Terran):
#    def __init__(self,name,hp):
#        super().__init__(name)
#        self.hp=hp
#    def attack(self):
#        print("총을쏩니다")
        

#def Attack(terran):
#    terran.attack()

#t1=Tank("tank",0)
#t2=Marine("marine",100)
#tlist=[Tank("tank",0), Tank("tank2",50), Marine("marine1",100)]
#for item in tlist:
#    Attack(item)
#Attack(t1)
#Attack(t2)
## 테란 객체 자체는 없지만 탱크, 마린이라는 인스턴스가 존재(테란은 객체를 만드는 클래스가 아니라는 얘기
##===============================================================

class MyList(list):
    name=""
    def __init__(self,name):
        super().__init__([])
        self.name=name
    def __str__(self):
        return self.name+":"+super().__str__()

list1=MyList("greenjoa")
list1.append(10)
list1.append(50)
list1.append(60)
list1.append(80)
list1.append(100)
print(list1)
print(dir(list1)) ## list1에서 사용할수있는 기능들(리스트의기능들)
##10+a1 : 씨쁠쁠에서는 전역으로 인자2개있는것 선언해서 해결
##파이썬에서는 10+a1은 __radd__연산자 호출
##a1+10은 __add__ 호출(클래스가 앞에 오면)