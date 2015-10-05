#class A():
#    def __init__(self,a):
#        self.a = a
#    def show(self):
#        print('show:',self.a)

#class B(A):
#    def __init__(self,b,**arg):
#        super().__init__(**arg)
#        self.b=b
#    def show(self):
#        print('show:',self.b)
#        super().show()

#class C(A):
#    def __init__(self,c,**arg):
#        super().__init__(**arg)
#        self.c=c
#    def show(self):
#        print('show:',self.c)
#        super().show()

#class D(B,C):
#    def __init__(self,d,**arg):
#        super().__init__(**arg)
#        self.d=d
#    def show(self):
#        print('show:',self.d)
#        super().show()

#data=D(a=1,b=2,c=3,d=4)
#data.show()

#lec04클래스 Private Variable
#오버라이딩시 인자 이름 등이 다 같아야하는데 여기 update에서는 다르다
#오버로딩된 함수들은 부모에 해당하는 함수에 찾아서 갈 수 없다
# update함수를 __붙여서 바꿈

#class Mapping:
#    def __init__(self,iterable):
#        self.items_list=[]
#        self.__update(iterable)

#    def update(self,iterable):
#        for item in iterable:
#            self.items_list.append(item)
#    __update=update

###super를 하게되면 부모를 호출할 수 있도록 해준다
#class MappingSubclass(Mapping):
#    def update(self,keys,values):
#        for item in zip(keys,values):
#            self.items_list.append(item)
#list1=[1,2,3,4]
#data=MappingSubclass(list1)
#print(data.items_list)

#data.update('5','a')
#print(data.items_list)
#import sys
#number1 = float(input("enter a number : "))
#number2 = float(input("enter a number : "))
#try :
#    result = number1 / number2
#    print(result)
#except ZeroDivisionError :
#    print("The answer is infinity")
#except :
#    error = sys.exc_info()[0]
#    print(error)
#   # sys.exit()#finally까지 다 수행후 종료
#finally:
#    print("Done")
import sys
try :
    result = number1 / number2
    print(result)
except :
    error = sys.exc_info()[0]
    print(error)
   # sys.exit()#finally까지 다 수행후 종료
finally:
    print("Done")
import csv
import xlsxwriter
fileName="201401.txt"
with open(fileName,"r") as myFile:
    newFileName=input("검색어를 입력하세요 : ")
    workbook=xlsxwriter.Workbook(newFileName+".xlsx")
    myNewFile=workbook.add_worksheet()
    i=1
    for currentRow in myFile:
        search=currentRow.split("|",4)
        if search[2]==newFileName:
            myNewFile.write('A'+str(i),search[0])
            myNewFile.write('B'+str(i),search[1])
            myNewFile.write('C'+str(i),search[2])
            myNewFile.write('D'+str(i),search[3])
            i+=1
    workbook.close()

          
