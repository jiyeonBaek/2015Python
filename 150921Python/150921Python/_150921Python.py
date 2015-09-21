#class Service:
#    secret = "영구는 배꼽이 두 개다"
#    def sum(self,a,b):
#        result=a+b
#        print("%s + %s = %s 입니다"%(a,b,result))


#pey = Service()
#print(pey.secret)
#pey.sum(1,1)
#Service.sum(pey,1,1)

#class Movie:
#    title=""
#    director=""
#    def __init__(self,title,director):
#        self.title=title
#        self.director=director
#    def showInfo(self):
#        print(self.title+" "+self.director)
#m1=Movie("암살","홍길동")
#m2=Movie("베테랑","김길동")
###Movie.__init__(m1,"암살","홍길동")
#m2.actor="유아인"
#Movie.showInfo(m2)


class Movie:
    '''영화 클래스 입니다.'''
    count=0
    title="암살"
    director="최동훈"
    def __init__(self,title,director):
        self.title=title
        self.director=director
        Movie.count+=1
        print(self.title+"생성자 호출")
    def __del__(self):
        print(self.title+"소멸자 호출")
    def showInfo(self):
        print(self.title+" "+self.director)
    
    @staticmethod
    def showCount1():
        print(Movie.count)
    
    @classmethod
    def showCount2(cls):
        print(cls.count) 

#print(m1.title)
#print(m1.__class__.title)
#print(m1.__doc__)
#m1=Movie("베테랑1","류승완1")
#m2=Movie("베테랑2","류승완2")
#m3=Movie("베테랑3","류승완3")
#m4=Movie("베테랑4","류승완4")
#print(type(m4))
#m4=m3 # 참조형 대입연산을 하게되면 똑같은 주소를 가리키고있는 형태가 된다
#print(id(m4)) #id : 주소
#print(id(m3))
#m4.showInfo()
m1=Movie("a","b")
m2=Movie("c","d")
m3=Movie("e","f")
m4=Movie("g","h")
m5=Movie("i","j")
Movie.showCount1()
Movie.showCount2()






#class MyClass:
#    data=1
#    def classTest(cls): # 클래스이름
#        print("class method")
#        print(cls.data)
#        print()
#    CTest = classmethod(classTest)

#    def staticTest():
#        print("static method")
#        print()
#    STest=staticmethod(staticTest)

#MyClass.CTest()
#MyClass.STest()