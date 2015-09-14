#def sum_and_mul(a,b):
#    return a+b,a*b

#data = sum_and_mul(3,4)
#sum,mul=sum_and_mul(3,4)
#print(data)
#print(sum)
#print(mul)

#def say_myself(name,old,man=True):
#    print("이름 : %s" %name)
#    print("나이 : %d" %old)
#    if man:
#        print("남자")
#    else:
#        print("여자")
#say_myself("greenjoa",23)

#def printData(data,level=0):
#    for item in data:
#        if isinstance(item,list):#item이 list이면
#            printData(item,level+1)
#        else:
#            for steps in range(level):
#                print("\t",end="")
#            print(item)

#import printData #모듈 이름

#data=["홍길동",["베테랑",["류승완","황정민","유아인"]],"고길동",["베테랑","밀양","암살"],"김길동",["미션임파서블"]]
#printData.printData(data)

import os
print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
#os.system("python setup.py sdist")
os.system("python setup.py install")